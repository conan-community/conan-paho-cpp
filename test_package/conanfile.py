import os
from conans import ConanFile, CMake, tools, RunEnvironment


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = [ "cmake", "cmake_paths" ]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*paho*.dll", dst="bin", src="bin")
        self.copy("*paho*.dylib*", dst="bin", src="lib")

    def test(self):
        if not tools.cross_building(self.settings):
            with tools.environment_append(RunEnvironment(self).vars):
                if self.settings.os == "Windows":
                    self.run(bin_path)
                elif self.settings.os == "Macos":
                    self.run("DYLD_LIBRARY_PATH=%s %s" % (os.environ.get('DYLD_LIBRARY_PATH', ''), os.path.join('build-with-cmake-generator', 'bin', 'test_package')))
#                    self.run("DYLD_LIBRARY_PATH=%s %s" % (os.environ.get('DYLD_LIBRARY_PATH', ''), os.path.join('build-with-cmake_paths-generator', 'bin', 'test_package')))
                else:
                    self.run("LD_LIBRARY_PATH=%s %s" % (os.environ.get('LD_LIBRARY_PATH', ''), os.path.join('build-with-cmake-generator', 'bin', 'test_package')))
#                    self.run("LD_LIBRARY_PATH=%s %s" % (os.environ.get('LD_LIBRARY_PATH', ''), os.path.join('build-with-cmake_paths-generator', 'bin', 'test_package')))

