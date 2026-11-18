import importlib.util
import json
import os
import plistlib
import sys
from xml.sax.saxutils import escape

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAMMAR = os.path.join(ROOT, "editors", "vscode", "syntaxes", "hyperez.tmLanguage.json")


def _load_grammar_module():
    path = os.path.join(ROOT, "editors", "vscode", "tools", "gen_grammar.py")
    spec = importlib.util.spec_from_file_location("gen_grammar", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_G = _load_grammar_module()

CONTROL = ["if", "else", "elif", "match", "for", "foreach", "in", "while", "repeat", "loop", "do", "break", "continue",
           "return", "await", "throw", "try", "catch", "finally", "step"]
DECLARATIONS = ["var", "let", "const", "function", "fn", "class", "struct", "interface", "enum", "event", "constructor",
                "import", "from", "as", "extends", "implements"]
MODIFIERS = ["public", "private", "protected", "static", "async", "get", "set"]
OPERATOR_WORDS = ["and", "or", "not", "is", "new", "on", "once", "emit", "priority"]
KEYWORDS = CONTROL + DECLARATIONS + MODIFIERS + OPERATOR_WORDS
CONSTANTS = ["true", "false", "null", "this", "super"]
TYPES = _G.PRIM.split("|")
BUILTIN_FUNCTIONS = _G.BUILTIN_FN.split("|")
BUILTIN_CLASSES = _G.BUILTIN_CLS.split("|")
BUILTINS = BUILTIN_FUNCTIONS + BUILTIN_CLASSES
EXTENSIONS = ["hez", "hz"]


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = text if isinstance(text, bytes) else text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return rel


def sublime():
    g = json.load(open(GRAMMAR, encoding="utf-8"))
    g.pop("$schema", None)
    g["uuid"] = "6f1c6f8e-7b3a-4c2e-9d2f-48a1a5c0f7e1"
    return write("editors/sublime/HyperEZ.tmLanguage", plistlib.dumps(g, sort_keys=False))


def notepadpp():
    styles = [
        ("DEFAULT", "1F2328", 0), ("COMMENTS", "008000", 2), ("LINE COMMENTS", "008000", 2), ("NUMBERS", "098658", 0),
        ("KEYWORDS1", "0000DC", 1), ("KEYWORDS2", "0000DC", 0), ("KEYWORDS3", "267F99", 0), ("KEYWORDS4", "795E26", 0),
        ("KEYWORDS5", "AF00DB", 1), ("KEYWORDS6", "000000", 0), ("KEYWORDS7", "000000", 0), ("KEYWORDS8", "000000", 0),
        ("OPERATORS", "1F2328", 0), ("FOLDER IN CODE1", "1F2328", 0), ("FOLDER IN CODE2", "000000", 0),
        ("FOLDER IN COMMENT", "000000", 0), ("DELIMITERS1", "A31515", 0), ("DELIMITERS2", "A31515", 0),
        ("DELIMITERS3", "000000", 0), ("DELIMITERS4", "000000", 0), ("DELIMITERS5", "000000", 0),
        ("DELIMITERS6", "000000", 0), ("DELIMITERS7", "000000", 0), ("DELIMITERS8", "000000", 0),
    ]
    style_xml = "\n".join(
        f'            <WordsStyle name="{n}" fgColor="{c}" bgColor="FFFFFF" fontStyle="{f}" nesting="0" />' for n, c, f in styles)
    lists = {
        "Keywords1": " ".join(DECLARATIONS + MODIFIERS + OPERATOR_WORDS),
        "Keywords2": " ".join(CONSTANTS),
        "Keywords3": " ".join(TYPES),
        "Keywords4": " ".join(BUILTINS),
        "Keywords5": " ".join(CONTROL),
    }
    kw_xml = "\n".join(f'            <Keywords name="Keywords{i}">{escape(lists.get(f"Keywords{i}", ""))}</Keywords>' for i in range(1, 9))
    xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<NotepadPlus>
    <UserLang name="HyperEZ" ext="{" ".join(EXTENSIONS)}" udlVersion="2.1">
        <Settings>
            <Global caseIgnored="no" allowFoldOfComments="yes" foldCompact="no" forcePureLC="0" decimalSeparator="0" />
            <Prefix Keywords1="no" Keywords2="no" Keywords3="no" Keywords4="no" Keywords5="no" Keywords6="no" Keywords7="no" Keywords8="no" />
        </Settings>
        <KeywordLists>
            <Keywords name="Comments">00// 01 02 03/* 04*/</Keywords>
            <Keywords name="Numbers, prefix1">0x 0b 0o</Keywords>
            <Keywords name="Numbers, prefix2"></Keywords>
            <Keywords name="Numbers, extras1">A B C D E F a b c d e f _</Keywords>
            <Keywords name="Numbers, extras2"></Keywords>
            <Keywords name="Numbers, suffix1"></Keywords>
            <Keywords name="Numbers, suffix2"></Keywords>
            <Keywords name="Numbers, range"></Keywords>
            <Keywords name="Operators1">( ) [ ] , ; : + - * / % = &lt; &gt; ! ? . | &amp; ^ ~</Keywords>
            <Keywords name="Operators2"></Keywords>
            <Keywords name="Folders in code1, open">{{</Keywords>
            <Keywords name="Folders in code1, middle"></Keywords>
            <Keywords name="Folders in code1, close">}}</Keywords>
            <Keywords name="Folders in code2, open"></Keywords>
            <Keywords name="Folders in code2, middle"></Keywords>
            <Keywords name="Folders in code2, close"></Keywords>
            <Keywords name="Folders in comment, open"></Keywords>
            <Keywords name="Folders in comment, middle"></Keywords>
            <Keywords name="Folders in comment, close"></Keywords>
{kw_xml}
            <Keywords name="Delimiters">00&quot; 01\\ 02&quot; 03&apos; 04\\ 05&apos; 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23</Keywords>
        </KeywordLists>
        <Styles>
{style_xml}
        </Styles>
    </UserLang>
</NotepadPlus>
"""
    return write("editors/notepad++/HyperEZ.xml", xml)


def vim():
    syn = f'''if exists("b:current_syntax")
  finish
endif

syn keyword hzConditional if else elif match
syn keyword hzRepeat for foreach in while repeat loop do break continue step
syn keyword hzStatement return await throw
syn keyword hzException try catch finally
syn keyword hzKeyword {" ".join(DECLARATIONS + MODIFIERS + OPERATOR_WORDS)}
syn keyword hzConstant {" ".join(CONSTANTS)}
syn keyword hzType {" ".join(TYPES)}
syn keyword hzBuiltin {" ".join(BUILTINS)}
syn match hzNumber "\\<\\(0[xX][0-9a-fA-F_]\\+\\|0[bB][01_]\\+\\|0[oO][0-7_]\\+\\|[0-9][0-9_]*\\(\\.[0-9_]\\+\\)\\=\\([eE][+-]\\=[0-9]\\+\\)\\=\\)\\>"
syn match hzClassName "\\<[A-Z][A-Za-z0-9_]*\\>"
syn region hzInterp matchgroup=hzInterpDelim start="${{" end="}}" contained contains=TOP
syn region hzString start=+"+ skip=+\\\\.+ end=+"+ contains=hzInterp,hzEscape
syn region hzString start=+'+ skip=+\\\\.+ end=+'+ contains=hzInterp,hzEscape
syn region hzString start=+"""+ end=+"""+ contains=hzInterp
syn region hzRawString start=+r"+ end=+"+
syn region hzRawString start=+r'+ end=+'+
syn match hzEscape "\\\\." contained
syn match hzDocComment "///.*$"
syn match hzComment "//.*$" contains=hzTodo
syn region hzComment start="/\\*" end="\\*/" contains=hzTodo
syn keyword hzTodo TODO FIXME PENDIENTE contained
syn match hzOperator "|>\\|=>\\|->\\|\\.\\.=\\|\\.\\.\\|??\\|?\\."

hi def link hzConditional Conditional
hi def link hzRepeat Repeat
hi def link hzStatement Statement
hi def link hzException Exception
hi def link hzKeyword Keyword
hi def link hzConstant Constant
hi def link hzType Type
hi def link hzClassName Type
hi def link hzBuiltin Function
hi def link hzNumber Number
hi def link hzString String
hi def link hzRawString String
hi def link hzEscape SpecialChar
hi def link hzInterpDelim Special
hi def link hzComment Comment
hi def link hzDocComment SpecialComment
hi def link hzTodo Todo
hi def link hzOperator Operator

let b:current_syntax = "hyperez"
'''
    det = "au BufRead,BufNewFile *.hez,*.hz setfiletype hyperez\n"
    ftp = """if exists("b:did_ftplugin")
  finish
endif
let b:did_ftplugin = 1
setlocal commentstring=//\\ %s
setlocal comments=s1:/*,mb:*,ex:*/,:///,://
setlocal expandtab shiftwidth=4 softtabstop=4 tabstop=4
setlocal suffixesadd=.hez,.hz
setlocal makeprg=hyper\\ check\\ %
setlocal errorformat=%f:%l:%c:\\ %m
let b:undo_ftplugin = "setlocal commentstring< comments< expandtab< shiftwidth< softtabstop< tabstop< suffixesadd< makeprg< errorformat<"
"""
    return [write("editors/vim/syntax/hyperez.vim", syn), write("editors/vim/ftdetect/hyperez.vim", det),
            write("editors/vim/ftplugin/hyperez.vim", ftp)]


def nano():
    def words(ws):
        return "\\<(" + "|".join(ws) + ")\\>"
    rc = f'''syntax hyperez "\\.(hez|hz)$"
header "^#!.*hyper"
comment "//"
color brightblue "{words(CONTROL)}"
color blue "{words(DECLARATIONS + MODIFIERS + OPERATOR_WORDS)}"
color cyan "{words(TYPES)}"
color brightyellow "{words(BUILTINS)}"
color magenta "{words(CONSTANTS)}"
color green "\\<(0[xX][0-9A-Fa-f_]+|0[bB][01_]+|0[oO][0-7_]+|[0-9][0-9_]*(\\.[0-9_]+)?([eE][+-]?[0-9]+)?)\\>"
color red ""([^"\\\\]|\\\\.)*"|'([^'\\\\]|\\\\.)*'"
color brightred "\\$\\{{[^}}]*\\}}"
color brightblack "//.*"
color brightblack start="/\\*" end="\\*/"
color ,green "[[:space:]]+$"
'''
    return write("editors/nano/hyperez.nanorc", rc)


def gtksourceview():
    def kw(ctx, style, ws):
        items = "\n".join(f"      <keyword>{w}</keyword>" for w in ws)
        return f'''    <context id="{ctx}" style-ref="{style}">
{items}
    </context>'''
    lang = f'''<?xml version="1.0" encoding="UTF-8"?>
<language id="hyperez" name="HyperEZ" version="2.0" _section="Source">
  <metadata>
    <property name="mimetypes">text/x-hyperez</property>
    <property name="globs">{";".join("*." + e for e in EXTENSIONS)}</property>
    <property name="line-comment-start">//</property>
    <property name="block-comment-start">/*</property>
    <property name="block-comment-end">*/</property>
  </metadata>
  <styles>
    <style id="comment" name="Comment" map-to="def:comment"/>
    <style id="doc-comment" name="Documentation comment" map-to="def:doc-comment"/>
    <style id="string" name="String" map-to="def:string"/>
    <style id="escape" name="Escape" map-to="def:special-char"/>
    <style id="interpolation" name="Interpolation" map-to="def:special-constant"/>
    <style id="number" name="Number" map-to="def:number"/>
    <style id="keyword" name="Keyword" map-to="def:keyword"/>
    <style id="control" name="Control" map-to="def:statement"/>
    <style id="constant" name="Constant" map-to="def:special-constant"/>
    <style id="type" name="Type" map-to="def:type"/>
    <style id="builtin" name="Builtin" map-to="def:builtin"/>
  </styles>
  <definitions>
    <context id="escape" style-ref="escape">
      <match>\\\\(u\\{{[0-9A-Fa-f]+\\}}|u[0-9A-Fa-f]{{4}}|.)</match>
    </context>
    <context id="interpolation" style-ref="interpolation">
      <start>\\$\\{{</start>
      <end>\\}}</end>
    </context>
    <context id="string-double" style-ref="string" end-at-line-end="true">
      <start>"</start>
      <end>"</end>
      <include>
        <context ref="escape"/>
        <context ref="interpolation"/>
      </include>
    </context>
    <context id="string-single" style-ref="string" end-at-line-end="true">
      <start>'</start>
      <end>'</end>
      <include>
        <context ref="escape"/>
        <context ref="interpolation"/>
      </include>
    </context>
    <context id="number" style-ref="number">
      <match extended="true">\\b(0[xX][0-9A-Fa-f_]+|0[bB][01_]+|0[oO][0-7_]+|[0-9][0-9_]*(\\.[0-9_]+)?([eE][+-]?[0-9]+)?)\\b</match>
    </context>
{kw("control", "control", CONTROL)}
{kw("keywords", "keyword", DECLARATIONS + MODIFIERS + OPERATOR_WORDS)}
{kw("constants", "constant", CONSTANTS)}
{kw("types", "type", TYPES)}
{kw("builtins", "builtin", BUILTINS)}
    <context id="hyperez" class="no-spell-check">
      <include>
        <context id="doc-comment" style-ref="doc-comment" end-at-line-end="true">
          <start>///</start>
        </context>
        <context ref="def:c-like-comment" style-ref="comment"/>
        <context ref="def:c-like-comment-multiline" style-ref="comment"/>
        <context ref="string-double"/>
        <context ref="string-single"/>
        <context ref="number"/>
        <context ref="control"/>
        <context ref="keywords"/>
        <context ref="constants"/>
        <context ref="types"/>
        <context ref="builtins"/>
      </include>
    </context>
  </definitions>
</language>
'''
    return write("editors/gtksourceview/hyperez.lang", lang)


def kate():
    def items(name, ws):
        body = "\n".join(f"        <item>{w}</item>" for w in ws)
        return f'''      <list name="{name}">
{body}
      </list>'''
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE language>
<language name="HyperEZ" section="Sources" version="2" kateversion="5.0" extensions="{";".join("*." + e for e in EXTENSIONS)}" mimetype="text/x-hyperez" indenter="cstyle" license="MIT">
  <highlighting>
{items("control", CONTROL)}
{items("keywords", DECLARATIONS + MODIFIERS + OPERATOR_WORDS)}
{items("constants", CONSTANTS)}
{items("types", TYPES)}
{items("builtins", BUILTINS)}
    <contexts>
      <context name="Normal" attribute="Normal Text" lineEndContext="#stay">
        <DetectSpaces/>
        <keyword attribute="Control Flow" context="#stay" String="control"/>
        <keyword attribute="Keyword" context="#stay" String="keywords"/>
        <keyword attribute="Constant" context="#stay" String="constants"/>
        <keyword attribute="Data Type" context="#stay" String="types"/>
        <keyword attribute="Built-in" context="#stay" String="builtins"/>
        <RegExpr attribute="Number" context="#stay" String="\\b(0[xX][0-9A-Fa-f_]+|0[bB][01_]+|0[oO][0-7_]+|[0-9][0-9_]*(\\.[0-9_]+)?([eE][+-]?[0-9]+)?)\\b"/>
        <StringDetect attribute="Doc Comment" context="LineComment" String="///"/>
        <Detect2Chars attribute="Comment" context="LineComment" char="/" char1="/"/>
        <Detect2Chars attribute="Comment" context="BlockComment" char="/" char1="*" beginRegion="Comment"/>
        <DetectChar attribute="String" context="StringDouble" char="&quot;"/>
        <DetectChar attribute="String" context="StringSingle" char="'"/>
        <DetectChar attribute="Symbol" context="#stay" char="{{" beginRegion="Brace"/>
        <DetectChar attribute="Symbol" context="#stay" char="}}" endRegion="Brace"/>
        <AnyChar attribute="Symbol" context="#stay" String=":!%&amp;()+,-/.*&lt;=&gt;?[]|~^;"/>
      </context>
      <context name="LineComment" attribute="Comment" lineEndContext="#pop"/>
      <context name="BlockComment" attribute="Comment" lineEndContext="#stay">
        <Detect2Chars attribute="Comment" context="#pop" char="*" char1="/" endRegion="Comment"/>
      </context>
      <context name="StringDouble" attribute="String" lineEndContext="#pop">
        <RegExpr attribute="Escape" context="#stay" String="\\\\."/>
        <Detect2Chars attribute="Interpolation" context="Interpolation" char="$" char1="{{"/>
        <DetectChar attribute="String" context="#pop" char="&quot;"/>
      </context>
      <context name="StringSingle" attribute="String" lineEndContext="#pop">
        <RegExpr attribute="Escape" context="#stay" String="\\\\."/>
        <Detect2Chars attribute="Interpolation" context="Interpolation" char="$" char1="{{"/>
        <DetectChar attribute="String" context="#pop" char="'"/>
      </context>
      <context name="Interpolation" attribute="Interpolation" lineEndContext="#pop">
        <DetectChar attribute="Interpolation" context="#pop" char="}}"/>
      </context>
    </contexts>
    <itemDatas>
      <itemData name="Normal Text" defStyleNum="dsNormal"/>
      <itemData name="Control Flow" defStyleNum="dsControlFlow"/>
      <itemData name="Keyword" defStyleNum="dsKeyword"/>
      <itemData name="Constant" defStyleNum="dsConstant"/>
      <itemData name="Data Type" defStyleNum="dsDataType"/>
      <itemData name="Built-in" defStyleNum="dsBuiltIn"/>
      <itemData name="Number" defStyleNum="dsDecVal"/>
      <itemData name="String" defStyleNum="dsString"/>
      <itemData name="Escape" defStyleNum="dsSpecialChar"/>
      <itemData name="Interpolation" defStyleNum="dsSpecialString"/>
      <itemData name="Comment" defStyleNum="dsComment"/>
      <itemData name="Doc Comment" defStyleNum="dsDocumentation"/>
      <itemData name="Symbol" defStyleNum="dsOperator"/>
    </itemDatas>
  </highlighting>
  <general>
    <comments>
      <comment name="singleLine" start="//"/>
      <comment name="multiLine" start="/*" end="*/" region="Comment"/>
    </comments>
    <keywords casesensitive="1"/>
  </general>
</language>
'''
    return write("editors/kate/hyperez.xml", xml)


def highlightjs():
    js = """(function () {
  function hyperez(hljs) {
    const INTERP = { className: 'subst', begin: /\\$\\{/, end: /\\}/, keywords: {} };
    const STRING = {
      className: 'string',
      variants: [
        { begin: /r"/, end: /"/ }, { begin: /r'/, end: /'/ },
        { begin: /\"\"\"/, end: /\"\"\"/, contains: [INTERP] },
        { begin: /"/, end: /"/, contains: [hljs.BACKSLASH_ESCAPE, INTERP] },
        { begin: /'/, end: /'/, contains: [hljs.BACKSLASH_ESCAPE, INTERP] }
      ]
    };
    const KEYWORDS = {
      keyword: %KEYWORDS%,
      literal: %CONSTANTS%,
      type: %TYPES%,
      built_in: %BUILTINS%
    };
    INTERP.keywords = KEYWORDS;
    INTERP.contains = [STRING, hljs.C_NUMBER_MODE];
    return {
      name: 'HyperEZ',
      aliases: ['hz', 'hez', 'hyperez'],
      keywords: KEYWORDS,
      contains: [
        hljs.COMMENT('///', '$', { className: 'doctag' }),
        hljs.C_LINE_COMMENT_MODE,
        hljs.C_BLOCK_COMMENT_MODE,
        STRING,
        { className: 'number', begin: /\\b(0[xX][0-9a-fA-F_]+|0[bB][01_]+|0[oO][0-7_]+|\\d[\\d_]*(\\.\\d[\\d_]*)?([eE][+-]?\\d+)?)\\b/ },
        { className: 'title.class', begin: /\\b[A-Z][A-Za-z0-9_]*\\b/ },
        { className: 'title.function', begin: /\\b[a-z_][A-Za-z0-9_]*(?=\\s*\\()/ },
        { className: 'operator', begin: /\\|>|=>|->|\\.\\.=?|\\?\\?|\\?\\./ }
      ]
    };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = hyperez;
  if (typeof hljs !== 'undefined') hljs.registerLanguage('hyperez', hyperez);
})();
"""
    js = (js.replace("%KEYWORDS%", json.dumps(" ".join(KEYWORDS)))
            .replace("%CONSTANTS%", json.dumps(" ".join(CONSTANTS)))
            .replace("%TYPES%", json.dumps(" ".join(TYPES)))
            .replace("%BUILTINS%", json.dumps(" ".join(BUILTINS))))
    return write("editors/highlightjs/hyperez.js", js)


def main():
    hechos = [sublime(), notepadpp(), *vim(), nano(), gtksourceview(), kate(), highlightjs()]
    for h in hechos:
        print("  " + h)


if __name__ == "__main__":
    main()
