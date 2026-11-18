#pragma once

#include "lang/vm/value.h"
#include "lang/vm/api.h"
#include "lang/sema/diagnostics.h"

#include <atomic>
#include <deque>
#include <random>

namespace hz {

struct Program;
struct ModuleUnit;
class Analyzer;

bool isLpoScript(const std::string& path);

struct NativeError { std::string message; };
struct PropagateError {};

enum class RunResult { Ok, Yield, Error };

struct ReplSession {
    ObjModule* module = nullptr;
    std::vector<std::string> globals;
    int start = 0;
    int echoSlot = -1;
};

extern std::atomic<bool> g_interrupt;

struct BuiltinInfo {
    std::string name;
    int index = -1;
    std::string doc;
};

class VM {
public:
    VM();
    ~VM();
    VM(const VM&) = delete;

    std::function<void(std::string_view)> printHook;
    std::function<std::string(const std::string&)> inputHook;
    std::function<bool(const std::string&, std::string&)> readSource;
    std::function<double()> clock;
    bool gameMode = false;
    std::string projectRoot;
    std::string projectHome();
    std::vector<std::string> searchPaths;
    std::vector<std::string> warnings;
    std::vector<std::string> scriptArgs;
    int testsPassed = 0, testsFailed = 0;
    ReplSession* repl = nullptr;

    ModuleUnit* compileFile(const std::string& path);
    ModuleUnit* compileSource(const std::string& path, const std::string& source, bool isEntry = true, bool codegen = true);
    bool unitHasErrors(ModuleUnit* unit);
    void printDiagnostics(ModuleUnit* unit, FILE* out, bool includeWarnings = true);
    bool loadPrelude();
    bool runModule(ModuleUnit* unit);
    bool drainScheduler();
    void pumpScheduler();
    bool hasPendingTasks() const;
    void cancelAllTasks();

    ModuleUnit* resolveImport(const std::string& path, bool isFile, const std::string& fromFile, std::string& error);
    Value libraryModule(const std::string& name);
    std::vector<std::string> libraryNames() const;
    std::vector<std::string> bundledLibraryNames() const;
    std::vector<std::unique_ptr<ModuleUnit>> units;
    ModuleUnit* preludeUnit = nullptr;
    ModuleUnit* entryUnit = nullptr;

    Value call(Value fn, int argc, const Value* args);
    Value call(Value fn, std::initializer_list<Value> args) { return call(fn, (int)args.size(), args.begin()); }
    Value callMethod(Value receiver, const char* name, int argc, const Value* args);
    Value callBound(Value method, Value self, int argc, const Value* args);
    void errorInit(ObjInstance* inst, Value message);
    ObjFiber* hostFiber = nullptr;
    bool tryCall(Value fn, int argc, const Value* args, Value* out = nullptr);
    Value getGlobal(ModuleUnit* unit, const std::string& name);
    Value findFunction(ModuleUnit* unit, const std::string& name);

    [[noreturn]] void raise(const std::string& msg);
    void reportError(const Value& err, FILE* out = stderr);
    std::string errorMessage(const Value& err);
    Value lastError;
    bool hadUncaught = false;
    std::function<bool(const std::string& message, const std::string& file, int line, int col,
                       const std::vector<std::string>& trace)> errorHook;

    ObjString* intern(std::string_view s);
    ObjString* internMove(std::string&& s);
    Value str(std::string_view s) { return Value::object(intern(s)); }
    ObjList* newList();
    ObjMap* newMap(bool isSet = false);
    ObjVec* newVec(int kind, double x = 0, double y = 0, double z = 0, double w = 0);
    ObjInstance* newInstance(ObjClass* cls);
    ObjForeign* newForeign(ObjClass* cls, void* ptr, void (*fin)(void*));
    ObjTask* newTask();
    ObjNative* newNative(const std::string& name, NativeFn fn, int minA = 0, int maxA = -1);
    ObjClass* newClass(const std::string& name);
    ObjRange* newRange(double a, double b, double step, bool inclusive);
    Value makeError(const std::string& msg, const std::string& kind = "Error");
    template <class T, class... A> T* alloc(A&&... a) {
        T* o = new T(std::forward<A>(a)...);
        o->next = objects;
        objects = o;
        bytesAllocated += sizeof(T) + 32;
        return o;
    }
    void pin(Value v);
    void unpin(Value v);
    void collectGarbage();
    void maybeGC() { if (bytesAllocated > nextGC && gcEnabled) collectGarbage(); }
    size_t bytesAllocated = 0, nextGC = 4 * 1024 * 1024;
    bool gcEnabled = true;
    std::vector<Value> tempRoots;
    std::vector<std::function<void(VM&)>> extraRoots;
    void markValue(const Value& v);
    void markObject(Obj* o);

    ObjModule* nativeModule(const std::string& name, const std::string& doc);
    ObjNative* defineFn(ObjModule* mod, const std::string& name, const std::string& sig, const std::string& doc, NativeFn fn,
                        const std::string& example = "");
    void defineProp(ObjModule* mod, const std::string& name, const std::string& type, const std::string& doc, NativeFn get,
                    NativeFn set = nullptr);
    void defineConst(ObjModule* mod, const std::string& name, Value v, const std::string& type, const std::string& doc);
    ObjNative* defineGlobalFn(const std::string& name, const std::string& sig, const std::string& doc, NativeFn fn,
                              const std::string& example = "");
    void defineGlobal(const std::string& name, Value v, const std::string& type, const std::string& doc);
    ObjClass* nativeClass(const std::string& name, const std::string& doc, NativeFn ctor = nullptr, const std::string& ctorSig = "");
    ObjNative* defineMethod(ObjClass* cls, const std::string& name, const std::string& sig, const std::string& doc, NativeFn fn);
    ObjNative* defineStatic(ObjClass* cls, const std::string& name, const std::string& sig, const std::string& doc, NativeFn fn);
    void defineClassProp(ObjClass* cls, const std::string& name, const std::string& type, const std::string& doc, NativeFn get,
                         NativeFn set = nullptr, bool isStatic = false);
    void addCatalogField(ObjClass* cls, const std::string& name, const std::string& type, const std::string& doc, bool readonly = false);
    ObjEvent* defineEvent(ObjModule* mod, const std::string& name, const std::string& params, const std::string& doc);
    void defineLibrary(const std::string& lib, const std::vector<std::string>& namespaces, const std::string& doc);
    std::vector<ApiEntry> catalog;
    std::vector<std::pair<std::string, std::string>> libraryDocs;
    std::unordered_map<std::string, std::vector<std::string>> libraryMembers;

    std::vector<Value> builtins;
    std::unordered_map<std::string, int> builtinIndex;
    int builtinSlot(const std::string& name);
    std::unordered_map<std::string, Value> libraries;

    ObjClass *textClass, *listClass, *mapClass, *setClass, *numberClass, *boolClass, *functionClass, *rangeClass,
        *taskClass, *eventClass, *subscriptionClass, *errorClass, *eventDataClass, *enumClass, *moduleClass,
        *enumValueClass;
    ObjClass* vecClass[5] = {};

    std::string toString(const Value& v, bool quoteStrings = false, int depth = 0);
    std::string typeName(const Value& v);
    bool isInstanceOf(const Value& v, std::string_view typeName);
    ObjClass* classOf(const Value& v);
    void flushOutput();
    void print(std::string_view s);
    void warn(const std::string& s);

    ObjFiber* fiber = nullptr;
    ObjFiber* mainFiber = nullptr;
    std::vector<ObjFiber*> fiberStack;
    std::deque<ObjFiber*> ready;
    std::vector<ObjTask*> timers;
    std::vector<ObjTask*> pendingTasks;
    uint64_t subscriptionCounter = 0;
    int nativeDepth = 0;
    double currentTime();

    void emitEvent(ObjEvent* ev, int argc, const Value* args, Value target = Value());
    ObjSubscription* subscribe(ObjEvent* ev, Value handler, bool once, double priority);
    Value eventPayload(ObjEvent* ev, int argc, const Value* args, Value target);

    ObjTask* waitTask(double seconds);
    void completeTask(ObjTask* t, Value result);
    void failTask(ObjTask* t, Value err);
    void wakeWaiters(ObjTask* t);

    RunResult run(int exitDepth);
    bool callValue(Value callee, int argc);
    bool throwValue(Value err);
    int currentExitDepth = 0;
    std::vector<std::string> lastTrace;
    struct Resume { ObjFiber* f; Value v; bool err; };
    std::deque<Resume> readyQ;
    std::vector<ObjTask*> nextFrameTasks;
    Value pendingError;
    bool hasPendingError = false;
    RunResult runFiber(ObjFiber* f, bool resume = false, Value v = Value(), bool isError = false);
    void resumeFiber(ObjFiber* f, Value v, bool isError);
    ObjUpvalue* captureUpvalue(int slot);
    void closeUpvalues(int fromSlot);
    Value getProperty(Value obj, ObjString* name, bool optional);
    void setProperty(Value obj, ObjString* name, Value v);
    Value getIndex(Value obj, Value idx);
    void setIndex(Value obj, Value idx, Value v);
    bool invoke(ObjString* name, int argc);
    Value bindMethod(Value receiver, Value method);
    bool instantiate(ObjClass* cls, int argc);
    Value importModule(const std::string& path);
    std::vector<std::string> stackTrace();
    std::string callArgsError;

    ObjNative* currentNative = nullptr;
    void* hostData = nullptr;

    std::string output;
    char lastOutputChar = '\n';
    bool outputToStdout = true;

    ObjString *s_constructor, *s_toString, *s_message, *s_stack, *s_name, *s_length, *s_iterator;

private:
    Obj* objects = nullptr;
    struct InternKey {
        std::string_view s;
        size_t h;
        bool operator==(const InternKey& o) const { return h == o.h && s == o.s; }
    };
    struct InternHash { size_t operator()(const InternKey& k) const noexcept { return k.h; } };
    std::unordered_map<InternKey, ObjString*, InternHash> strings;
    std::vector<Obj*> gray;
    std::unordered_map<Obj*, int> pinned;
    void blacken(Obj* o);
    void sweep();
    void registerCore();
    ApiEntry& addCatalog(ApiKind kind, const std::string& owner, const std::string& name, const std::string& sig,
                         const std::string& doc);
public:
    bool callClosure(ObjClosure* c, int argc);
    bool callNative(ObjNative* n, int argc);
    bool callMethodValue(Value method, int argc);
    bool startAsync(ObjClosure* c, int argc);
    bool reorderNamed(Value callee, int& argc, ObjList* names);
    Value arith(uint8_t op, Value a, Value b);
    bool objectsEqual(const Value& a, const Value& b);
    bool contains(Value container, Value item);
    void push(Value v) { fiber->ensure(1); fiber->stack[fiber->sp++] = v; }
    friend struct VMRunner;
};

struct NativeScope {
    VM& vm;
    ObjNative* prev;
    NativeScope(VM& v, ObjNative* n) : vm(v), prev(v.currentNative) { v.currentNative = n; }
    ~NativeScope() { vm.currentNative = prev; }
};

double argNum(VM& vm, Value* args, int argc, int i, const char* fname, double def = NAN);
std::string argStr(VM& vm, Value* args, int argc, int i, const char* fname, const char* def = nullptr);
bool argBool(Value* args, int argc, int i, bool def);
ObjList* argList(VM& vm, Value* args, int argc, int i, const char* fname);
ObjMap* argMap(VM& vm, Value* args, int argc, int i, const char* fname);
ObjVec* argVec(VM& vm, Value* args, int argc, int i, const char* fname, int kind);
Value optArg(Value* args, int argc, int i);
Value optField(VM& vm, ObjMap* opts, const char* key);

std::mt19937_64& randomEngine();
double randomUnit();
long long randomBetween(long long lo, long long hi);
void registerStdlib(VM& vm);
void registerStdlibExtra(VM& vm);
void registerMathTypes(VM& vm);

}
