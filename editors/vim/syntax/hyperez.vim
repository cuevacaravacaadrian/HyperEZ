if exists("b:current_syntax")
  finish
endif

syn keyword hzConditional if else elif match
syn keyword hzRepeat for foreach in while repeat loop do break continue step
syn keyword hzStatement return await throw
syn keyword hzException try catch finally
syn keyword hzKeyword var let const function fn class struct interface enum event constructor import from as extends implements public private protected static async get set and or not is new on once emit priority
syn keyword hzConstant true false null this super
syn keyword hzType number int float double text string char bool boolean list array map dict set any object void null function Function Task Promise Range Event Subscription
syn keyword hzBuiltin print println write input len typeof str toNumber toInt assert assertEqual assertThrows test exit range time now wait nextFrame spawn delay tick warn createEvent off abs sqrt pow floor ceil round sign min max clamp lerp sin cos tan asin acos atan atan2 hypot exp log log10 radians degrees random randomInt randomChoice randomSeed remap wrap approach smoothstep chance distance isNaN awaitAll awaitAny parseInt gcd lcm factorial isPrime primes divisors cbrt trunc fract sinh cosh tanh randomGaussian noise chr ord Console File System JSON Vec2 Vec3 Color Error EventData HyperCore HyperMath Process Path Time Bytes Hash Base64 Regex Http Matrix Image ProcessHandle
syn match hzNumber "\<\(0[xX][0-9a-fA-F_]\+\|0[bB][01_]\+\|0[oO][0-7_]\+\|[0-9][0-9_]*\(\.[0-9_]\+\)\=\([eE][+-]\=[0-9]\+\)\=\)\>"
syn match hzClassName "\<[A-Z][A-Za-z0-9_]*\>"
syn region hzInterp matchgroup=hzInterpDelim start="${" end="}" contained contains=TOP
syn region hzString start=+"+ skip=+\\.+ end=+"+ contains=hzInterp,hzEscape
syn region hzString start=+'+ skip=+\\.+ end=+'+ contains=hzInterp,hzEscape
syn region hzString start=+"""+ end=+"""+ contains=hzInterp
syn region hzRawString start=+r"+ end=+"+
syn region hzRawString start=+r'+ end=+'+
syn match hzEscape "\\." contained
syn match hzDocComment "///.*$"
syn match hzComment "//.*$" contains=hzTodo
syn region hzComment start="/\*" end="\*/" contains=hzTodo
syn keyword hzTodo TODO FIXME PENDIENTE contained
syn match hzOperator "|>\|=>\|->\|\.\.=\|\.\.\|??\|?\."

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
