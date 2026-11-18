# Instrucciones de la máquina virtual

El compilador traduce cada función a una lista de instrucciones (bytecode) para una máquina de pila.
Cada instrucción ocupa un byte y puede llevar operandos de 8 bits (`u8`) o 16 bits (`u16`).
La columna «Operandos y pila» indica qué lee de la pila y qué deja (`a b -> r`).

> Este archivo se genera con `python tools/gen_docs.py` a partir de `src/lang/compiler/bytecode.h`.

| # | Instrucción | Operandos y pila |
|---|---|---|
| 0 | `OP_CONST` |  |
| 1 | `OP_GET_LOCAL` |  |
| 2 | `OP_SET_LOCAL` |  |
| 3 | `OP_GET_UPVAL` |  |
| 4 | `OP_SET_UPVAL` |  |
| 5 | `OP_GET_GLOBAL` |  |
| 6 | `OP_SET_GLOBAL` |  |
| 7 | `OP_DEFINE_GLOBAL` |  |
| 8 | `OP_GET_BUILTIN` |  |
| 9 | `OP_GET_PROP` |  |
| 10 | `OP_SET_PROP` |  |
| 11 | `OP_GET_INDEX` |  |
| 12 | `OP_SET_INDEX` |  |
| 13 | `OP_GET_SUPER` |  |
| 14 | `OP_IN` |  |
| 15 | `OP_IS` |  |
| 16 | `OP_JUMP` |  |
| 17 | `OP_JUMP_IF_FALSE` |  |
| 18 | `OP_JUMP_IF_TRUE` |  |
| 19 | `OP_LOOP` |  |
| 20 | `OP_CALL` |  |
| 21 | `OP_CALL_NAMED` |  |
| 22 | `OP_CALL_SPREAD` |  |
| 23 | `OP_INVOKE` |  |
| 24 | `OP_SUPER_INVOKE` |  |
| 25 | `OP_SUPER_CALL` |  |
| 26 | `OP_CLOSURE` |  |
| 27 | `OP_CLOSE_UPVALUE` |  |
| 28 | `OP_RETURN` |  |
| 29 | `OP_CLASS` |  |
| 30 | `OP_INHERIT` |  |
| 31 | `OP_METHOD` |  |
| 32 | `OP_FIELD` |  |
| 33 | `OP_IMPLEMENTS` |  |
| 34 | `OP_LIST` |  |
| 35 | `OP_LIST_APPEND` |  |
| 36 | `OP_LIST_EXTEND` |  |
| 37 | `OP_MAP` |  |
| 38 | `OP_RANGE` |  |
| 39 | `OP_RANGE_STEP` |  |
| 40 | `OP_ITER_PREP` |  |
| 41 | `OP_ITER_NEXT` |  |
| 42 | `OP_FOR_CHECK` |  |
| 43 | `OP_FOR_INCR` |  |
| 44 | `OP_REPEAT_PREP` |  |
| 45 | `OP_REPEAT_NEXT` |  |
| 46 | `OP_TRY` |  |
| 47 | `OP_END_TRY` |  |
| 48 | `OP_THROW` |  |
| 49 | `OP_AWAIT` |  |
| 50 | `OP_EMIT` |  |
| 51 | `OP_ON` |  |
| 52 | `OP_ENUM` |  |
| 53 | `OP_EVENT` |  |
| 54 | `OP_IMPORT` |  |
| 55 | `OP_IMPORT_NAME` |  |
| 56 | `OP_TO_STRING` |  |
| 57 | `OP_CONCAT` |  |
| 58 | `OP_CHECK_TYPE` |  |
| 59 | `OP_DEFAULT_ARG` |  |
| 60 | `OP_MATCH_TEST` |  |
| 61 | `OP_SUPER_INIT_AUTO` |  |
| 62 | `OP_CHECK_RETURN` |  |
| 63 | `OP_SLIDE` |  |
| 64 | `OP_JUMP_IF_NOT_LT` |  |
| 65 | `OP_JUMP_IF_NOT_LE` |  |
| 66 | `OP_JUMP_IF_NOT_GT` |  |
| 67 | `OP_JUMP_IF_NOT_GE` |  |
| 68 | `OP_JUMP_IF_NOT_EQ` |  |
| 69 | `OP_JUMP_IF_NOT_NE` |  |
| 70 | `OP_FOR_NEXT` |  |
| 71 | `OP_CHECK_NUMBER` |  |
| 72 | `OP_SET_LOCAL_POP` |  |
| 73 | `OP_FOR_CHECK_V` |  |
| 74 | `OP_FOR_NEXT_V` |  |

Hay 75 instrucciones.
