# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/tom/Coding/PicoSystem/ToolChain/pico-sdk/tools/pioasm"
  "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm"
  "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm"
  "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm/tmp"
  "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm/src/PioasmBuild-stamp"
  "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm/src"
  "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm/src/PioasmBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm/src/PioasmBuild-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/tom/Coding/PicoSystem/CPP_Projects/PicoSystem_InfoNes/build/pioasm/src/PioasmBuild-stamp${cfgdir}") # cfgdir has leading slash
endif()
