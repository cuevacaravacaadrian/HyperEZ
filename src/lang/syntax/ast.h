#pragma once

#include "lang/syntax/lexer.h"

namespace hz {

struct Symbol;
struct ClassInfo;
struct Type;
using TypeP = std::shared_ptr<Type>;

struct TypeRef {
    std::string name;
    std::vector<std::unique_ptr<TypeRef>> args;
    bool nullable = false;
    SrcLoc loc;
    std::string toString() const;
};
using TypeRefP = std::unique_ptr<TypeRef>;

enum class Visibility : uint8_t { Public, Private, Protected };
enum class DeclKind : uint8_t { Var, Let, Const };

enum class VarKind : uint8_t {
    Unresolved,
    Local,
    Upvalue,
    Global,
    Builtin,
    ThisMember,
    StaticMember,
};

struct Resolution {
    VarKind kind = VarKind::Unresolved;
    int index = -1;
    VarKind thisKind = VarKind::Unresolved;
    int thisIndex = -1;
    VarKind classKind = VarKind::Unresolved;
    int classIndex = -1;
};

enum class ExprKind : uint8_t {
    Number, String, Bool, Null, Ident, This, Super, List, Map, Unary, Binary, Logical, Ternary,
    Call, Member, Index, Lambda, Range, Await, Is, Match, Assign, IncDec, On,
};

struct Expr {
    ExprKind kind;
    SrcLoc loc;
    TypeP type;
    explicit Expr(ExprKind k, SrcLoc l) : kind(k), loc(l) {}
    virtual ~Expr() = default;
};
using ExprP = std::unique_ptr<Expr>;

struct Stmt;
using StmtP = std::unique_ptr<Stmt>;
struct FuncDecl;

struct NumberExpr : Expr { double value; bool isInt; NumberExpr(SrcLoc l, double v, bool i) : Expr(ExprKind::Number, l), value(v), isInt(i) {} };
struct StringExpr : Expr {
    struct Part { bool isExpr = false; std::string text; ExprP expr; };
    std::vector<Part> parts;
    StringExpr(SrcLoc l) : Expr(ExprKind::String, l) {}
    bool isPlain() const { return parts.size() == 1 && !parts[0].isExpr; }
};
struct BoolExpr : Expr { bool value; BoolExpr(SrcLoc l, bool v) : Expr(ExprKind::Bool, l), value(v) {} };
struct NullExpr : Expr { NullExpr(SrcLoc l) : Expr(ExprKind::Null, l) {} };
struct IdentExpr : Expr {
    std::string name;
    Resolution res;
    Symbol* sym = nullptr;
    IdentExpr(SrcLoc l, std::string n) : Expr(ExprKind::Ident, l), name(std::move(n)) {}
};
struct ThisExpr : Expr { Resolution res; ThisExpr(SrcLoc l) : Expr(ExprKind::This, l) {} };
struct SuperExpr : Expr { std::string member; Resolution thisRes; SuperExpr(SrcLoc l) : Expr(ExprKind::Super, l) {} };
struct ListExpr : Expr { std::vector<ExprP> items; std::vector<bool> spread; ListExpr(SrcLoc l) : Expr(ExprKind::List, l) {} };
struct MapExpr : Expr {
    std::vector<std::pair<ExprP, ExprP>> entries;
    MapExpr(SrcLoc l) : Expr(ExprKind::Map, l) {}
};
struct UnaryExpr : Expr { Tok op; ExprP operand; UnaryExpr(SrcLoc l, Tok o, ExprP e) : Expr(ExprKind::Unary, l), op(o), operand(std::move(e)) {} };
struct BinaryExpr : Expr {
    Tok op; ExprP left, right; bool negate = false;
    BinaryExpr(SrcLoc l, Tok o, ExprP a, ExprP b) : Expr(ExprKind::Binary, l), op(o), left(std::move(a)), right(std::move(b)) {}
};
struct LogicalExpr : Expr {
    Tok op; ExprP left, right;
    LogicalExpr(SrcLoc l, Tok o, ExprP a, ExprP b) : Expr(ExprKind::Logical, l), op(o), left(std::move(a)), right(std::move(b)) {}
};
struct TernaryExpr : Expr { ExprP cond, then, otherwise; TernaryExpr(SrcLoc l) : Expr(ExprKind::Ternary, l) {} };
struct Arg { std::string name; SrcLoc nameLoc; ExprP value; bool spread = false; };
struct CallExpr : Expr {
    ExprP callee;
    std::vector<Arg> args;
    bool isNew = false;
    bool optional = false;
    bool hasNamed() const { for (auto& a : args) if (!a.name.empty()) return true; return false; }
    CallExpr(SrcLoc l) : Expr(ExprKind::Call, l) {}
};
struct MemberExpr : Expr {
    ExprP object; std::string name; SrcLoc nameLoc; bool optional = false;
    Symbol* sym = nullptr;
    MemberExpr(SrcLoc l) : Expr(ExprKind::Member, l) {}
};
struct IndexExpr : Expr { ExprP object, index; bool optional = false; IndexExpr(SrcLoc l) : Expr(ExprKind::Index, l) {} };
struct LambdaExpr : Expr { std::unique_ptr<FuncDecl> fn; LambdaExpr(SrcLoc l) : Expr(ExprKind::Lambda, l) {} ~LambdaExpr() override; };
struct RangeExpr : Expr { ExprP start, end, step; bool inclusive = false; RangeExpr(SrcLoc l) : Expr(ExprKind::Range, l) {} };
struct AwaitExpr : Expr { ExprP operand; AwaitExpr(SrcLoc l) : Expr(ExprKind::Await, l) {} };
struct IsExpr : Expr { ExprP operand; TypeRefP target; bool negate = false; IsExpr(SrcLoc l) : Expr(ExprKind::Is, l) {} };
struct MatchArm {
    std::vector<ExprP> patterns;
    bool isElse = false;
    ExprP guard;
    ExprP body;
    std::vector<StmtP> block;
    bool hasBlock = false;
    SrcLoc loc;
};
struct MatchExpr : Expr {
    ExprP subject; std::vector<MatchArm> arms; int subjectSlot = -1;
    MatchExpr(SrcLoc l) : Expr(ExprKind::Match, l) {}
    ~MatchExpr() override;
};
struct AssignExpr : Expr { Tok op; ExprP target, value; AssignExpr(SrcLoc l, Tok o) : Expr(ExprKind::Assign, l), op(o) {} };
struct IncDecExpr : Expr { ExprP target; bool inc; bool prefix; IncDecExpr(SrcLoc l) : Expr(ExprKind::IncDec, l) {} };
struct OnExpr : Expr {
    ExprP event; ExprP priority; bool once = false;
    std::unique_ptr<FuncDecl> handler;
    OnExpr(SrcLoc l) : Expr(ExprKind::On, l) {}
    ~OnExpr() override;
};

enum class StmtKind : uint8_t {
    Expr, Var, Block, If, While, ForRange, ForEach, Repeat, Break, Continue, Return,
    Function, Class, Interface, Enum, Event, Emit, Try, Throw, Import,
};

struct Stmt {
    StmtKind kind;
    SrcLoc loc;
    explicit Stmt(StmtKind k, SrcLoc l) : kind(k), loc(l) {}
    virtual ~Stmt() = default;
};

struct LocalInfo { int slot; bool captured; };

struct ExprStmt : Stmt {
    ExprP expr;
    bool isBlockValue = false;
    ExprStmt(SrcLoc l, ExprP e) : Stmt(StmtKind::Expr, l), expr(std::move(e)) {}
};
struct VarStmt : Stmt {
    DeclKind declKind = DeclKind::Var;
    std::string name; SrcLoc nameLoc;
    TypeRefP typeAnn; ExprP init;
    Visibility vis = Visibility::Public;
    Resolution res;
    Symbol* sym = nullptr;
    std::string doc;
    VarStmt(SrcLoc l) : Stmt(StmtKind::Var, l) {}
};
struct BlockStmt : Stmt {
    std::vector<StmtP> body;
    std::vector<LocalInfo> locals;
    SrcLoc endLoc;
    BlockStmt(SrcLoc l) : Stmt(StmtKind::Block, l) {}
};
struct IfStmt : Stmt { ExprP cond; StmtP then; StmtP otherwise; IfStmt(SrcLoc l) : Stmt(StmtKind::If, l) {} };
struct WhileStmt : Stmt { ExprP cond; StmtP body; WhileStmt(SrcLoc l) : Stmt(StmtKind::While, l) {} };
struct ForRangeStmt : Stmt {
    std::string var; SrcLoc varLoc;
    ExprP start, end, step; bool inclusive = false;
    StmtP body;
    int slotCounter = -1, slotEnd = -1, slotStep = -1, slotVar = -1;
    bool varCaptured = false;
    Symbol* sym = nullptr;
    ForRangeStmt(SrcLoc l) : Stmt(StmtKind::ForRange, l) {}
};
struct ForEachStmt : Stmt {
    std::string var, var2; SrcLoc varLoc, var2Loc;
    ExprP iterable; StmtP body;
    int slotIter = -1, slotState = -1, slotVar = -1, slotVar2 = -1;
    bool varCaptured = false, var2Captured = false;
    Symbol* sym = nullptr; Symbol* sym2 = nullptr;
    ForEachStmt(SrcLoc l) : Stmt(StmtKind::ForEach, l) {}
};
struct RepeatStmt : Stmt { ExprP count; StmtP body; int slotCounter = -1; RepeatStmt(SrcLoc l) : Stmt(StmtKind::Repeat, l) {} };
struct BreakStmt : Stmt { BreakStmt(SrcLoc l) : Stmt(StmtKind::Break, l) {} };
struct ContinueStmt : Stmt { ContinueStmt(SrcLoc l) : Stmt(StmtKind::Continue, l) {} };
struct ReturnStmt : Stmt { ExprP value; ReturnStmt(SrcLoc l) : Stmt(StmtKind::Return, l) {} };
struct ThrowStmt : Stmt { ExprP value; ThrowStmt(SrcLoc l) : Stmt(StmtKind::Throw, l) {} };
struct FuncDecl;
struct TryStmt : Stmt {
    std::unique_ptr<BlockStmt> body;
    std::string catchVar; SrcLoc catchLoc; TypeRefP catchType;
    std::unique_ptr<BlockStmt> catchBody;
    std::unique_ptr<BlockStmt> finallyBody;
    std::unique_ptr<FuncDecl> finallyFn;
    int catchSlot = -1; bool catchCaptured = false;
    Symbol* catchSym = nullptr;
    TryStmt(SrcLoc l) : Stmt(StmtKind::Try, l) {}
    ~TryStmt() override;
};

enum class FuncKind : uint8_t { Function, Method, Constructor, Getter, Setter, Lambda, Handler, Script, FieldInit };

struct Param {
    std::string name; SrcLoc loc;
    TypeRefP type; ExprP def; bool rest = false;
    int slot = -1; bool captured = false;
    Symbol* sym = nullptr;
};

struct UpvalueDesc { bool isLocal; int index; std::string name; };

struct FuncDecl {
    FuncKind kind = FuncKind::Function;
    std::string name; SrcLoc loc, nameLoc;
    std::vector<Param> params;
    TypeRefP ret;
    std::unique_ptr<BlockStmt> body;
    ExprP exprBody;
    bool isAsync = false, isStatic = false;
    Visibility vis = Visibility::Public;
    std::string doc;
    std::vector<UpvalueDesc> upvalues;
    int maxSlots = 0;
    bool hasExplicitSuperCall = false;
    bool containsAwait = false;
    Resolution res;
    Symbol* sym = nullptr;
    ClassInfo* owner = nullptr;
};

struct FuncStmt : Stmt { std::unique_ptr<FuncDecl> fn; FuncStmt(SrcLoc l) : Stmt(StmtKind::Function, l) {} };

struct FieldDecl {
    std::string name; SrcLoc loc;
    DeclKind declKind = DeclKind::Var;
    TypeRefP type; ExprP init;
    bool isStatic = false;
    Visibility vis = Visibility::Public;
    std::string doc;
    Symbol* sym = nullptr;
};

struct ClassStmt : Stmt {
    std::string name; SrcLoc nameLoc;
    bool isStruct = false;
    std::string superName; SrcLoc superLoc; ExprP superExpr;
    std::vector<std::pair<std::string, SrcLoc>> interfaces;
    std::vector<FieldDecl> fields;
    std::vector<std::unique_ptr<FuncDecl>> methods;
    std::unique_ptr<FuncDecl> ctor;
    std::unique_ptr<FuncDecl> fieldInit;
    std::unique_ptr<FuncDecl> staticInit;
    std::string doc;
    Resolution res;
    Symbol* sym = nullptr;
    ClassInfo* info = nullptr;
    SrcLoc endLoc;
    ClassStmt(SrcLoc l) : Stmt(StmtKind::Class, l) {}
};

struct InterfaceMethod { std::string name; SrcLoc loc; std::vector<Param> params; TypeRefP ret; };
struct InterfaceStmt : Stmt {
    std::string name; SrcLoc nameLoc;
    std::vector<InterfaceMethod> methods;
    std::vector<std::pair<std::string, SrcLoc>> extends;
    std::string doc;
    Resolution res; Symbol* sym = nullptr;
    InterfaceStmt(SrcLoc l) : Stmt(StmtKind::Interface, l) {}
};

struct EnumMember { std::string name; SrcLoc loc; ExprP value; double resolved = 0; std::string strValue; bool isString = false; Symbol* sym = nullptr; };
struct EnumStmt : Stmt {
    std::string name; SrcLoc nameLoc;
    std::vector<EnumMember> members;
    std::string doc;
    Resolution res; Symbol* sym = nullptr;
    EnumStmt(SrcLoc l) : Stmt(StmtKind::Enum, l) {}
};

struct EventStmt : Stmt {
    std::string name; SrcLoc nameLoc;
    std::vector<Param> params;
    std::string doc;
    Resolution res; Symbol* sym = nullptr;
    EventStmt(SrcLoc l) : Stmt(StmtKind::Event, l) {}
};

struct EmitStmt : Stmt { ExprP event; std::vector<Arg> args; EmitStmt(SrcLoc l) : Stmt(StmtKind::Emit, l) {} };

struct ImportStmt : Stmt {
    std::string path;
    bool isFile = false;
    bool importAll = false;
    std::string alias; SrcLoc aliasLoc;
    std::vector<std::pair<std::string, SrcLoc>> names;
    std::vector<std::string> nameAliases;
    std::vector<Resolution> nameRes;
    std::vector<Symbol*> nameSyms;
    Resolution res; Symbol* sym = nullptr;
    std::string resolvedPath;
    ImportStmt(SrcLoc l) : Stmt(StmtKind::Import, l) {}
};

struct Program {
    std::string file;
    std::string source;
    std::vector<StmtP> body;
    std::vector<Comment> comments;
    std::unique_ptr<FuncDecl> script;
    int globalCount = 0;
    std::vector<std::string> globalNames;
};

}
