from os.path import join
from conan import ConanFile
from conan.tools.files import get, copy
from conan.tools.files import apply_conandata_patches, export_conandata_patches
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.microsoft.visual import is_msvc

required_conan_version = ">=1.53.0"


class LibboardConan(ConanFile):
    name = "libboard"
    version = "0.9.4"
    license = "LGPL-3.0"
    url = "https://github.com/sintef-ocean/conan-libboard"
    homepage = "https://github.com/c-koi/libboard"
    author = "SINTEF Ocean"
    description = \
        "The LibBoard C++ library allows the drawing of Postscript, SVG, " \
        "and FIG (XFig) vector graphics using the C++ programming language."
    topics = ("vector graphics", "Postscript", "SVG", "XFig")
    settings = "os", "compiler", "build_type", "arch"
    package_type = "static-library"
    options = {
        "fPIC": [True, False],
    }
    default_options = {
        "fPIC": True,
    }

    def export_sources(self):
        export_conandata_patches(self)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self, src_folder="src")

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        apply_conandata_patches(self)
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

        copy(self, "LICENSE", self.source_folder,
             join(self.package_folder, "licenses"))

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "Libboard")
        self.cpp_info.set_property("cmake_target_name", "Libboard::Libboard")

        if is_msvc(self) or (self.settings.os == "Windows" and self.settings.compiler == "clang"):
            self.cpp_info.libs = ["libboard"]
        else:
            self.cpp_info.libs = ["board"]
        if(self.settings.build_type) == "Debug":
            self.cpp_info.libs[0] += "_d"
