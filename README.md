# conan-paho-cpp

![conan-paho-cpp image](/images/conan-paho-cpp.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/paho-cpp%3Aconan/images/download.svg)](https://bintray.com/conan-community/conan/paho-cpp%3Aconan/_latestVersion)
[![Build Status](https://travis-ci.org/conan-community/conan-paho-cpp.svg?branch=stable%2F1.0.0)](https://travis-ci.org/conan-community/conan-paho-cpp)
[![Build status](https://ci.appveyor.com/api/projects/status/b15m00302vlt843c/branch/stable/1.0.0?svg=true)](https://ci.appveyor.com/project/danimtb/conan-paho-cpp/branch/stable/1.0.0)

[Conan.io](https://conan.io) package for [paho.mqtt.cpp](https://github.com/eclipse/paho.mqtt.cpp) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/conan-community/conan/paho-cpp%3Aconan).

## For Users: Use this package

### Basic setup

    $ conan install paho-cpp/1.0.0@conan/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    paho-cpp/1.0.0@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
