# -*- coding: utf-8 -*-
import os
from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration


class PahocppConan(ConanFile):
    name = "paho-cpp"
    version = "1.0.1"
    license = "EPL-1.0"
    homepage = "https://github.com/eclipse/paho.mqtt.cpp"
    description = "The open-source client implementations of MQTT and MQTT-SN"
    url = "https://github.com/conan-community/conan-paho-cpp"
    author = "Conan Communty"
    topics = ("conan", "paho-cpp", "paho", "mqtt", "mqtt-sn")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "SSL": [True, False],
               "fPIC": [True, False]}
    default_options = {"shared": False, "SSL": False, "fPIC": True}
    generators = "cmake"
    exports = "LICENSE"
    exports_sources = [
        "CMakeLists.txt",
        "0001-fix-cmake-module-path.patch",
        "0002-fix-cmake-find-paho-mqtt-c-static.patch",
        "0003-fix-paho-mqtt-cpp-config-cmake.patch"
    ]
    requires = "paho-c/1.3.0@conan/stable"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
        self.options["paho-c"].SSL = self.options.SSL

    def configure(self):
        if self.settings.os == "Windows" and self.options.shared:
            raise ConanInvalidConfiguration("Paho cpp can not be built as shared on Windows.")

    @property
    def _source_subfolder(self):
        return "sources"

    def source(self):
        sha256 = "42faf223bf78300eaaa8fa7d0e1bc039ff5de2890a392b83973f1be59aa68ea3"
        tools.get("%s/archive/v%s.zip" % (self.homepage, self.version), sha256=sha256)
        os.rename("paho.mqtt.cpp-%s" % self.version, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["PAHO_BUILD_DOCUMENTATION"] = False
        cmake.definitions["PAHO_BUILD_SAMPLES"] = False
        cmake.definitions["PAHO_BUILD_STATIC"] = not self.options.shared
        cmake.definitions["PAHO_BUILD_SHARED"] = self.options.shared
        cmake.definitions["PAHO_WITH_SSL"] = self.options.SSL
        cmake.configure()
        return cmake

    def build(self):
        tools.patch(base_path=self._source_subfolder, patch_file="0001-fix-cmake-module-path.patch")
        tools.patch(base_path=self._source_subfolder, patch_file="0002-fix-cmake-find-paho-mqtt-c-static.patch")
        tools.patch(base_path=self._source_subfolder, patch_file="0003-fix-paho-mqtt-cpp-config-cmake.patch")
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        for license_file in ["edl-v10", "epl-v10", "notice.html"]:
            self.copy(license_file, src=self._source_subfolder, dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
