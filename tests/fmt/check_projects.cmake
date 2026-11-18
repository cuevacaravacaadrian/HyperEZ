file(REMOVE_RECURSE "${TMP}")
file(MAKE_DIRECTORY "${TMP}")
foreach(kind juego app ia script web sitio)
  execute_process(COMMAND "${HYPER}" new "p-${kind}" --tipo ${kind} WORKING_DIRECTORY "${TMP}"
                  RESULT_VARIABLE rc OUTPUT_QUIET ERROR_VARIABLE err)
  if(rc)
    message(FATAL_ERROR "hyper new --tipo ${kind} falló: ${err}")
  endif()
  execute_process(COMMAND "${HYPER}" check . WORKING_DIRECTORY "${TMP}/p-${kind}" RESULT_VARIABLE rc OUTPUT_VARIABLE out ERROR_VARIABLE err)
  if(rc)
    message(FATAL_ERROR "El proyecto '${kind}' tiene errores:\n${out}${err}")
  endif()
  execute_process(COMMAND "${HYPER}" test WORKING_DIRECTORY "${TMP}/p-${kind}" RESULT_VARIABLE rc OUTPUT_VARIABLE out ERROR_VARIABLE err)
  if(rc)
    message(FATAL_ERROR "Las pruebas del proyecto '${kind}' fallan:\n${out}${err}")
  endif()
endforeach()

set(P "${TMP}/p-juego")
file(WRITE "${P}/hypertools/saludo.hez" "// Saluda
import saludos
from jugador import Jugador
print(saludos.hola(System.args[0]), Path.name(System.projectDir), typeof(Jugador))
")
file(WRITE "${P}/hyperlibs/saludos/main.hez" "function hola(n: text): text { return \"hola \" + n }
")
execute_process(COMMAND "${HYPER}" tool saludo Ana WORKING_DIRECTORY "${P}/hypertests" RESULT_VARIABLE rc OUTPUT_VARIABLE out ERROR_VARIABLE err)
if(rc OR NOT out MATCHES "hola Ana p-juego class")
  message(FATAL_ERROR "hyper tool / hyperlibs / hypercode no funcionan:
${out}${err}")
endif()
execute_process(COMMAND "${HYPER}" tool WORKING_DIRECTORY "${P}" RESULT_VARIABLE rc OUTPUT_VARIABLE out ERROR_VARIABLE err)
if(rc OR NOT out MATCHES "saludo")
  message(FATAL_ERROR "hyper tool no lista las herramientas:
${out}${err}")
endif()
file(REMOVE_RECURSE "${TMP}")
message(STATUS "los 6 tipos de proyecto y las carpetas de HyperEZ funcionan")
