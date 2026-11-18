#pragma once

#include <filesystem>
#include <string>
#include <vector>

namespace hz {

std::filesystem::path findEditorSupportDir(const std::filesystem::path& hyperExe);

std::vector<std::string> installEditorSupport(const std::filesystem::path& supportDir, bool install);

}
