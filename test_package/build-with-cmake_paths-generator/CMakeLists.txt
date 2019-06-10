project(test_package_cmake_paths)
cmake_minimum_required(VERSION 2.8.11)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

## --- C++11 build flags ---

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Set compiler and linker flags (stdc++ version, arch, etc.).
# Usually when using conan_paths, these are set by developer or build environment.
# But we use conanbuildinfo.cmake as we are building from conan
# and we need to make a universal CMakeLists.txt for testing purposes.
# Without this fix, CMake will use automatically detected stdc++, arch, etc.
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_output_dirs_setup()
conan_set_flags("")
conan_set_flags("_RELEASE")
conan_set_flags("_DEBUG")
conan_set_libcxx()
conan_set_vs_runtime()


find_package(PahoMqttCpp REQUIRED)
find_package(Threads REQUIRED)

file(GLOB SOURCE_FILES ../*.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME test_package)
if(PAHO_BUILD_STATIC)
	target_link_libraries(${PROJECT_NAME} PahoMqttCpp::paho-mqttpp3-static)
else()
	target_link_libraries(${PROJECT_NAME} PahoMqttCpp::paho-mqttpp3)
endif()
target_link_libraries(${PROJECT_NAME} Threads::Threads)

