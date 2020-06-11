#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools


class LibboardConan(ConanFile):
    name = "libboard"
    version = "0.9.4"
    license = "LGPL-3.0"
    url = "https://github.com/sintef-ocean/conan-libboard"
    homepage = "https://github.com/c-koi/libboard"
    author = "Joakim Haugen (joakim.haugen@gmail.com)"
    description = \
        "The LibBoard C++ library allows the drawing of Postscript, SVG, " \
        "and FIG (XFig) vector graphics using the C++ programming language."
    topics = ("vector graphics", "Postscript", "SVG", "XFig")
    settings = "os", "compiler", "build_type", "arch"
    exports = ["patch/*"]
    generators = ("cmake_paths", "cmake_find_package")
    source_subfolder = "libboard"
    build_subfolder = "build_subfolder"

    def _config_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder,
                        build_folder=self.build_subfolder)
        return cmake

    def source(self):

        self.run("git clone --depth 1 -b v{0} https://github.com/c-koi/libboard.git"\
                 .format(self.version))
        tools.patch(patch_file="patch/CMakeLists.patch",
                    base_path=self.source_subfolder)
        tools.patch(patch_file="patch/PathBoundaries.patch",
                    base_path=self.source_subfolder)
        tools.patch(patch_file="patch/Shapes.patch",
                    base_path=self.source_subfolder)
        tools.patch(patch_file="patch/Tools.patch",
                    base_path=self.source_subfolder)

    def build(self):
        cmake = self._config_cmake()
        cmake.build()

    def package(self):
        cmake = self._config_cmake()
        cmake.install()
        self.copy("LICENSE", dst="licenses", src=self.source_subfolder,
                  ignore_case=True, keep_path=False)

    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["libboard"]
        else:
            self.cpp_info.libs = ["board"]
        if(self.settings.build_type) == "Debug":
            self.cpp_info.libs[0] += "_d"
