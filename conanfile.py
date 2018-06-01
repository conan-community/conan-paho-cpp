import os
from conans import ConanFile, CMake, tools


class PahocppConan(ConanFile):
    name = "paho-cpp"
    version = "1.0.0"
    license = "EPL-1.0"
    homepage = "https://github.com/eclipse/paho.mqtt.cpp"
    description = """The Eclipse Paho project provides open-source client implementations of MQTT
and MQTT-SN messaging protocols aimed at new, existing, and emerging applications for the Internet
of Things (IoT)"""
    url = "https://github.com/conan-community/conan-paho-cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "SSL": [True, False]}
    default_options = "shared=False", "SSL=False"
    generators = "cmake"
    exports = "LICENSE", "cmakelists.patch"
    requires = "paho-c/1.2.0@conan/stable"

    def configure(self):
        self.options["paho-c"].SSL = self.options.SSL
        self.options["paho-c"].asynchronous = True

    @property
    def source_subfolder(self):
        return "sources"

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.homepage, self.version))
        os.rename("paho.mqtt.cpp-%s" % self.version, self.source_subfolder)
        cmakelists_path = "%s/CMakeLists.txt" % self.source_subfolder
        tools.replace_in_file(cmakelists_path,
                              "project(\"paho-mqtt-cpp\" LANGUAGES CXX)",
                              """project(\"paho-mqtt-cpp\" LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()""")
        tools.patch(patch_file="cmakelists.patch")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PAHO_BUILD_DOCUMENTATION"] = False
        cmake.definitions["PAHO_BUILD_SAMPLES"] = False
        cmake.definitions["PAHO_BUILD_STATIC"] = not self.options.shared
        cmake.definitions["PAHO_BUILD_SHARED"] = self.options.shared
        cmake.definitions["PAHO_WITH_SSL"] = self.options.SSL
        cmake.configure(source_folder=self.source_subfolder)
        cmake.build()

    def package(self):
        self.copy("edl-v10", src=self.source_subfolder, dst="licenses", keep_path=False)
        self.copy("epl-v10", src=self.source_subfolder, dst="licenses", keep_path=False)
        self.copy("notice.html", src=self.source_subfolder, dst="licenses", keep_path=False)
        self.copy("*.h", dst="include", src="%s/src" % self.source_subfolder)
        pattern = "*paho-mqttpp3"
        for extension in [".a", ".dll.a", ".lib", ".dll", ".dylib", ".*.dylib", ".so*"]:
            self.copy(pattern + extension, dst="bin" if extension.endswith("dll") else "lib",
                      keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
