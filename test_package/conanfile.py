import os
from conans import ConanFile, CMake, tools


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = [ "cmake", "cmake_paths" ]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join('build-with-cmake-generator', 'bin', 'test_package')
            bin_path = os.path.join('build-with-cmake_paths-generator', 'bin', 'test_package')
            self.run(bin_path, run_environment=True)
