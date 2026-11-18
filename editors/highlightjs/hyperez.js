(function () {
  function hyperez(hljs) {
    const INTERP = { className: 'subst', begin: /\$\{/, end: /\}/, keywords: {} };
    const STRING = {
      className: 'string',
      variants: [
        { begin: /r"/, end: /"/ }, { begin: /r'/, end: /'/ },
        { begin: /"""/, end: /"""/, contains: [INTERP] },
        { begin: /"/, end: /"/, contains: [hljs.BACKSLASH_ESCAPE, INTERP] },
        { begin: /'/, end: /'/, contains: [hljs.BACKSLASH_ESCAPE, INTERP] }
      ]
    };
    const KEYWORDS = {
      keyword: "if else elif match for foreach in while repeat loop do break continue return await throw try catch finally step var let const function fn class struct interface enum event constructor import from as extends implements public private protected static async get set and or not is new on once emit priority",
      literal: "true false null this super",
      type: "number int float double text string char bool boolean list array map dict set any object void null function Function Task Promise Range Event Subscription",
      built_in: "print println write input len typeof str toNumber toInt assert assertEqual assertThrows test exit range time now wait nextFrame spawn delay tick warn createEvent off abs sqrt pow floor ceil round sign min max clamp lerp sin cos tan asin acos atan atan2 hypot exp log log10 radians degrees random randomInt randomChoice randomSeed remap wrap approach smoothstep chance distance isNaN awaitAll awaitAny parseInt gcd lcm factorial isPrime primes divisors cbrt trunc fract sinh cosh tanh randomGaussian noise chr ord Console File System JSON Vec2 Vec3 Color Error EventData HyperCore HyperMath Process Path Time Bytes Hash Base64 Regex Http Matrix Image ProcessHandle"
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
        { className: 'number', begin: /\b(0[xX][0-9a-fA-F_]+|0[bB][01_]+|0[oO][0-7_]+|\d[\d_]*(\.\d[\d_]*)?([eE][+-]?\d+)?)\b/ },
        { className: 'title.class', begin: /\b[A-Z][A-Za-z0-9_]*\b/ },
        { className: 'title.function', begin: /\b[a-z_][A-Za-z0-9_]*(?=\s*\()/ },
        { className: 'operator', begin: /\|>|=>|->|\.\.=?|\?\?|\?\./ }
      ]
    };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = hyperez;
  if (typeof hljs !== 'undefined') hljs.registerLanguage('hyperez', hyperez);
})();
