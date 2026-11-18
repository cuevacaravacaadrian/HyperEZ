#pragma once

#include <cstdint>
#include <string>

namespace hz {

class VM;
struct ObjFunction;

std::string disassemble(VM& vm, ObjFunction* fn, bool recursive = true);

int operandBytes(uint8_t op);

}
