#pragma once

#include "core/common.h"
#include "core/process.h"

namespace hz {

class VM;

void setupVM(VM& vm);

int runRepl();
int runWatch(const std::string& file, const std::vector<std::string>& args);

struct ProjectFile { std::string path, content; };
std::vector<std::string> projectKinds();
std::vector<ProjectFile> projectFiles(const std::string& kind, const std::string& title);
std::string projectTemplateMain(const std::string& title);
std::string projectTemplateModule();
std::string projectTemplateTest();
std::string projectTemplateReadme(const std::string& title);

std::string generateApiMarkdown(VM& vm);

int runLanguageServer();
std::string languageServerMessage(const std::string& message);
int nativeBuild(const std::vector<std::string>& args);

#ifdef _WIN32
bool registerFileTypes(const std::string& hyperExe, bool install, const std::wstring& classesRoot = L"Software\\Classes",
                       bool quiet = false);
#elif !defined(__APPLE__)
bool registerFileTypes(const std::string& hyperExe, bool install);
#endif

}
