#pragma once

#include <string>
#include <string_view>

namespace hz {

struct FormatResult {
    bool ok = false;
    bool changed = false;
    std::string text;
    std::string error;
};

FormatResult formatSource(std::string_view source);

}
