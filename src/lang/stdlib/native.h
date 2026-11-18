#pragma once

#include "lang/vm/vm.h"

#include <filesystem>

namespace hz {

#define NATIVE(name) static Value name(VM& vm, int argc, Value* args)
#define UNUSED (void)vm; (void)argc; (void)args

struct TempRoot {
    VM& vm;
    TempRoot(VM& v, Obj* o) : vm(v) { vm.tempRoots.push_back(Value::object(o)); }
    ~TempRoot() { vm.tempRoots.pop_back(); }
    TempRoot(const TempRoot&) = delete;
};

std::string resolvePath(VM& vm, const std::string& p);
inline std::filesystem::path FP(const std::string& s) { return std::filesystem::path((const char8_t*)s.c_str()); }
inline std::string U8(const std::filesystem::path& p) {
    auto u = p.u8string();
    return std::string((const char*)u.data(), u.size());
}

inline ObjModule* existingModule(VM& vm, const std::string& name) {
    Value v = vm.builtins[vm.builtinSlot(name)];
    return isObjType(v, OT::Module) ? static_cast<ObjModule*>(v.o) : vm.nativeModule(name, "");
}

inline void put(VM& vm, ObjMap* m, const char* key, Value v) { m->set(vm.str(key), v); }

std::vector<std::string> argStrList(VM& vm, Value* args, int argc, int i, const char* fname);

void registerSystemLibs(VM& vm);
void registerBinaryLibs(VM& vm);
void registerRegex(VM& vm);
void registerNet(VM& vm);
void registerMatrix(VM& vm);
void registerImage(VM& vm);
void registerServer(VM& vm);
void registerMore(VM& vm);

Value newBytes(VM& vm, std::vector<uint8_t> data);
std::vector<uint8_t>* bytesData(VM& vm, const Value& v);

}
