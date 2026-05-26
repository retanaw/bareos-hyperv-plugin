cmake_minimum_required(VERSION 3.20)
project(hyper-v-fd CXX)

# ── hyper-v.cc viene del checkout de bareos/bareos ──────────────────────────
set(BAREOS_SRC "${CMAKE_SOURCE_DIR}/bareos-src" CACHE PATH "bareos source root")

set(PLUGIN_SRC "${BAREOS_SRC}/core/src/win32/plugins/filed/hyper-v.cc")
if(NOT EXISTS "${PLUGIN_SRC}")
  message(FATAL_ERROR "hyper-v.cc not found at ${PLUGIN_SRC}")
endif()

add_library(hyper-v-fd SHARED "${PLUGIN_SRC}")

target_include_directories(hyper-v-fd PRIVATE
  "${BAREOS_SRC}/core/src"
  "${BAREOS_SRC}/core/src/include"
  "${BAREOS_SRC}/core/src/win32/include"
  "${BAREOS_SRC}/core/src/win32/compat/include"
)

# Windows SDK libs needed by the Hyper-V plugin
target_link_libraries(hyper-v-fd PRIVATE
  virtdisk
  wbemuuid
  Shell32
  Pathcch
)

set_target_properties(hyper-v-fd PROPERTIES
  PREFIX ""
  SUFFIX ".dll"
  OUTPUT_NAME "hyper-v-fd"
)
