project(test_package_cmake_paths)
cmake_minimum_required(VERSION 2.8.11)

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

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(PahoMqttCpp REQUIRED)
find_package(Threads REQUIRED)

add_executable(${PROJECT_NAME} ${CMAKE_SOURCE_DIR}/test_package.cpp)
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME test_package)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 11 CXX_STANDARD_REQUIRED 11)
if(PAHO_BUILD_STATIC)
	target_link_libraries(${PROJECT_NAME} PahoMqttCpp::paho-mqttpp3-static)
else()
	target_link_libraries(${PROJECT_NAME} PahoMqttCpp::paho-mqttpp3)
endif()
target_link_libraries(${PROJECT_NAME} Threads::Threads)
