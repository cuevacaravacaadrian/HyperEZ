#include "tools/platform/editors.h"

#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <system_error>

#ifdef _WIN32
#include <cwchar>
#endif

namespace fs = std::filesystem;

namespace hz {

namespace {

fs::path envPath(const char* name) {
#ifdef _WIN32
    std::wstring w(name, name + std::strlen(name));
    const wchar_t* v = _wgetenv(w.c_str());
    return v && *v ? fs::path(v) : fs::path();
#else
    const char* v = std::getenv(name);
    return v && *v ? fs::path(v) : fs::path();
#endif
}

fs::path testRoot() { return envPath("HYPEREZ_EDITORS_HOME"); }

fs::path home() {
    if (fs::path t = testRoot(); !t.empty()) return t;
#ifdef _WIN32
    return envPath("USERPROFILE");
#else
    return envPath("HOME");
#endif
}

#ifdef _WIN32
fs::path appData() { return testRoot().empty() ? envPath("APPDATA") : home() / "AppData" / "Roaming"; }
fs::path localAppData() { return testRoot().empty() ? envPath("LOCALAPPDATA") : home() / "AppData" / "Local"; }
#else
fs::path configHome() {
    fs::path x = testRoot().empty() ? envPath("XDG_CONFIG_HOME") : fs::path();
    return x.empty() ? home() / ".config" : x;
}
fs::path dataHome() {
    fs::path x = testRoot().empty() ? envPath("XDG_DATA_HOME") : fs::path();
    return x.empty() ? home() / ".local" / "share" : x;
}
#endif

bool isDir(const fs::path& p) {
    std::error_code ec;
    return !p.empty() && fs::is_directory(p, ec);
}

bool isFile(const fs::path& p) {
    std::error_code ec;
    return !p.empty() && fs::is_regular_file(p, ec);
}

#ifndef _WIN32
bool onPath(const std::string& program) {
    if (!testRoot().empty()) return false;
    std::stringstream ss(envPath("PATH").string());
    std::string dir;
    while (std::getline(ss, dir, ':'))
        if (!dir.empty() && isFile(fs::path(dir) / program)) return true;
    return false;
}
#endif

bool copyFile(const fs::path& from, const fs::path& to) {
    std::error_code ec;
    fs::create_directories(to.parent_path(), ec);
    return fs::copy_file(from, to, fs::copy_options::overwrite_existing, ec);
}

void removeFile(const fs::path& p) {
    std::error_code ec;
    fs::remove(p, ec);
}

#ifndef _WIN32
void removeIfEmpty(const fs::path& dir) {
    std::error_code ec;
    if (isDir(dir) && fs::is_empty(dir, ec)) fs::remove(dir, ec);
}

#endif

struct Target {
    std::string editor;
    bool present;
    std::vector<std::pair<std::string, fs::path>> files;
};

void addVim(std::vector<Target>& out, const std::string& name, const fs::path& root, bool present) {
    Target t{name, present, {}};
    for (const char* kind : {"syntax", "ftdetect", "ftplugin"})
        t.files.push_back({std::string("vim/") + kind + "/hyperez.vim", root / kind / "hyperez.vim"});
    out.push_back(std::move(t));
}

std::vector<Target> targets() {
    std::vector<Target> t;
#ifdef _WIN32
    fs::path npp = appData() / "Notepad++";
    t.push_back({"Notepad++", isDir(npp), {{"notepad++/HyperEZ.xml", npp / "userDefineLangs" / "HyperEZ.xml"}}});
    for (const char* v : {"Sublime Text", "Sublime Text 3"}) {
        fs::path st = appData() / v;
        t.push_back({v, isDir(st), {{"sublime/HyperEZ.tmLanguage", st / "Packages" / "User" / "HyperEZ.tmLanguage"}}});
    }
    fs::path vimfiles = home() / "vimfiles";
    addVim(t, "Vim", vimfiles, isDir(vimfiles) || isFile(home() / "_vimrc") || isFile(home() / ".vimrc"));
    fs::path nvim = localAppData() / "nvim";
    addVim(t, "Neovim", nvim, isDir(nvim));
#else
#ifdef __APPLE__
    fs::path stRoot = home() / "Library" / "Application Support";
#else
    fs::path stRoot = configHome();
#endif
    for (const char* v : {"Sublime Text", "sublime-text", "Sublime Text 3", "sublime-text-3"}) {
        fs::path st = stRoot / v;
        if (isDir(st)) t.push_back({"Sublime Text", true, {{"sublime/HyperEZ.tmLanguage", st / "Packages" / "User" / "HyperEZ.tmLanguage"}}});
    }
    fs::path vim = home() / ".vim";
    addVim(t, "Vim", vim, isDir(vim) || isFile(home() / ".vimrc") || onPath("vim"));
    fs::path nvim = configHome() / "nvim";
    addVim(t, "Neovim", nvim, isDir(nvim) || onPath("nvim"));
#ifndef __APPLE__
    fs::path share = dataHome();
    Target gtk{"gedit / GNOME Text Editor", true, {}};
    for (const char* v : {"gtksourceview-3.0", "gtksourceview-4", "gtksourceview-5"})
        gtk.files.push_back({"gtksourceview/hyperez.lang", share / v / "language-specs" / "hyperez.lang"});
    t.push_back(std::move(gtk));
    t.push_back({"Kate", true, {{"kate/hyperez.xml", share / "org.kde.syntax-highlighting" / "syntax" / "hyperez.xml"}}});
#endif
#endif
    return t;
}

#ifndef _WIN32
fs::path nanorcFile() { return home() / ".nanorc"; }
fs::path nanoSyntaxFile() { return dataHome() / "hyperez" / "hyperez.nanorc"; }

std::string includeLine() { return "include \"" + nanoSyntaxFile().string() + "\""; }

bool setNanoInclude(bool add) {
    std::string text;
    {
        std::ifstream in(nanorcFile(), std::ios::binary);
        if (in) { std::stringstream ss; ss << in.rdbuf(); text = ss.str(); }
    }
    std::string line = includeLine();
    std::stringstream ss(text);
    std::string l, kept;
    bool found = false;
    while (std::getline(ss, l)) {
        if (l == line) { found = true; if (!add) continue; }
        kept += l + "\n";
    }
    if (add && found) return true;
    if (!add && !found) return true;
    if (add) kept += line + "\n";
    std::ofstream out(nanorcFile(), std::ios::binary | std::ios::trunc);
    out << kept;
    return (bool)out;
}
#endif

}

fs::path findEditorSupportDir(const fs::path& hyperExe) {
    std::error_code ec;
    fs::path exe = fs::weakly_canonical(hyperExe, ec);
    if (ec) exe = hyperExe;
    fs::path bin = exe.parent_path();
    for (const fs::path& c : {bin.parent_path() / "editors", bin.parent_path() / "share" / "hyperez" / "editors",
                              bin.parent_path().parent_path() / "editors", bin / "editors"})
        if (isFile(c / "notepad++" / "HyperEZ.xml")) return c;
    return {};
}

std::vector<std::string> installEditorSupport(const fs::path& supportDir, bool install) {
    std::vector<std::string> done;
    if (install && supportDir.empty()) return done;
    for (auto& t : targets()) {
        bool any = false;
        for (auto& [rel, dest] : t.files) {
            if (!install) {
                if (isFile(dest)) { removeFile(dest); any = true; }
                continue;
            }
            if (!t.present) continue;
            if (copyFile(supportDir / rel, dest)) any = true;
        }
        if (any && (done.empty() || done.back() != t.editor)) done.push_back(t.editor);
    }
#ifndef _WIN32
    bool nano = isFile(nanorcFile()) || onPath("nano");
    if (install && nano && copyFile(supportDir / "nano" / "hyperez.nanorc", nanoSyntaxFile()) && setNanoInclude(true))
        done.push_back("nano");
    if (!install && isFile(nanoSyntaxFile())) {
        setNanoInclude(false);
        removeFile(nanoSyntaxFile());
        removeIfEmpty(nanoSyntaxFile().parent_path());
        done.push_back("nano");
    }
#endif
    return done;
}

}
