#pragma once
#ifdef _WIN32

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif
#ifndef NOMINMAX
#define NOMINMAX
#endif
#include <windows.h>
#include <shlobj.h>

#include <string>

namespace hz::win {

std::wstring widen(const std::string& s);
std::string narrow(const std::wstring& w);
std::wstring backslashes(std::wstring p);

bool setValue(HKEY root, const std::wstring& key, const std::wstring& name, const std::wstring& value, DWORD type = REG_SZ);
bool setDword(HKEY root, const std::wstring& key, const std::wstring& name, DWORD value);
bool getValue(HKEY root, const std::wstring& key, const std::wstring& name, std::wstring& out, DWORD* type = nullptr);
bool deleteTree(HKEY root, const std::wstring& key);
std::wstring knownFolder(REFKNOWNFOLDERID id);

bool registerFileTypes(const std::wstring& hyperExe, bool install, const std::wstring& classesRoot = L"Software\\Classes",
                       const std::wstring& iconFile = {});
bool registerLanguage(const std::wstring& hyperExe, bool install, const std::wstring& softwareKey = L"Software\\HyperEZ");
bool updateUserPath(const std::wstring& dir, bool add, const std::wstring& envKey = L"Environment");
bool createShortcut(const std::wstring& lnk, const std::wstring& target, const std::wstring& args, const std::wstring& desc,
                    const std::wstring& icon, int iconIndex, const std::wstring& workDir);
std::wstring findVSCode();
std::wstring findVSCodeCli();
void notifyAssociationsChanged();
void broadcastEnvironmentChange();

}
#endif
