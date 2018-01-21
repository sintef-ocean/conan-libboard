#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools

class LibboardConan(ConanFile):
    name = "libboard"
    version = "0.9.4"
    license = "LGPL-3.0-only"
    url = "https://github.com/joakimono/conan-libboard"
    homepage = "https://github.com/c-koi/libboard"
    author = "Joakim Haugen (joakim.haugen@gmail.com)"
    description = "The LibBoard C++ library allows the drawing of Postscript, SVG, and FIG (XFig) vector graphics using the C++ programming language."
    settings = "os", "compiler", "build_type", "arch"
    exports = ["patch/*"]
    generators = "cmake"
    source_subfolder = "libboard"
    build_subfolder = "build_subfolder"

    def source(self):

        self.run("git clone --depth 1 -b v{0} https://github.com/c-koi/libboard.git".format(self.version))
        tools.patch(patch_file="patch/CMakeLists.patch", base_path=self.source_subfolder)
        tools.patch(patch_file="patch/PathBoundaries.patch", base_path=self.source_subfolder)
        tools.patch(patch_file="patch/Shapes.patch", base_path=self.source_subfolder)
        tools.patch(patch_file="patch/Tools.patch", base_path=self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder, build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()
        cmake.test()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self.source_subfolder,
                  ignore_case=True, keep_path=False)

    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["libboard"]
        else:
            self.cpp_info.libs = ["board"]
        if(self.settings.build_type) == "Debug":
            self.cpp_info.libs[0] += "_d"
        
