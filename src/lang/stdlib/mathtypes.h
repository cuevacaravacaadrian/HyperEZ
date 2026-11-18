#pragma once

#include "lang/vm/vm.h"

namespace hz {

struct RGBA { float r = 1, g = 1, b = 1, a = 1; };

RGBA toColor(VM& vm, Value v, const char* fname, RGBA def = {});
bool parseColorName(const std::string& s, RGBA& out);
Value makeColor(VM& vm, RGBA c);

}
