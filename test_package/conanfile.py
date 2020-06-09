#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibboardTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake_paths", "cmake_find_package")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        pass

    def test(self):
        program = 'example'
        if self.settings.os == "Windows":
            program += '.exe'
            test_path = os.path.join(self.build_folder,
                                     str(self.settings.build_type))
        else:
            test_path = '.' + os.sep

        self.run(os.path.join(test_path, program))
