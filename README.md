[![Download](https://api.bintray.com/packages/sintef-ocean/conan/libboard%3Asintef/images/download.svg)](https://bintray.com/sintef-ocean/conan/libboard%3Asintef/_latestVersion)
[![GCC Conan](https://github.com/sintef-ocean/conan-libboard/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-libboard/actions?query=workflow%3A"GCC+Conan")

[Conan.io](https://conan.io) recipe for [libboard](https://github.com/c-koi/libboard).

The recipe generates library packages, which can be found at [Bintray](https://bintray.com/sintef-ocean/conan/libboard%3Asintef).
The package is usually consumed using the `conan install` command or a *conanfile.txt*.

## How to use this package

1. Add remote to conan's package [registry.txt](http://docs.conan.io/en/latest/reference/config_files/registry.txt.html):

   ```bash
   $ conan remote add sintef https://api.bintray.com/conan/sintef-ocean/conan
   ```

2. Using *conanfile.txt* in your project with *cmake*

   Add a [*conanfile.txt*](http://docs.conan.io/en/latest/reference/conanfile_txt.html) to your project. This file describes dependencies and your configuration of choice, e.g.:

   ```
   [requires]
   libboard/[>=0.9.4]@sintef/stable

   [options]


   [imports]
   licenses, * -> ./licenses @ folder=True

   [generators]
   cmake_paths
   cmake_find_package
   ```

   Insert into your *CMakeLists.txt* something like the following lines:
   ```cmake
   cmake_minimum_required(VERSION 3.1.2)
   project(TheProject CXX)

   include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

   find_package(libboard MODULE REQUIRED)

   add_executable(the_executor code.cpp)
   target_link_libraries(the_executor libboard::libboard)
   ```
   Then, do
   ```bash
   $ mkdir build && cd build
   $ conan install ..
   ```
   You can now continue with the usual dance with cmake commands for configuration and compilation. For details on how to use conan, please consult [Conan.io docs](http://docs.conan.io/en/latest/)

## Package options

None

## Known recipe issues

None
