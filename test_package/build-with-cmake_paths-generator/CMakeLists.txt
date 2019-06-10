project(test_package_cmake_paths)
cmake_minimum_required(VERSION 2.8.11)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

## --- C++11 build flags ---

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

file(GLOB SOURCE_FILES ../*.cpp)


find_package(PahoMqttCpp REQUIRED)
find_package(Threads REQUIRED)


add_executable(${PROJECT_NAME} ${SOURCE_FILES})
set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME test_package)
if(PAHO_BUILD_STATIC)
	target_link_libraries(${PROJECT_NAME} PahoMqttCpp::paho-mqttpp3-static)
else()
	target_link_libraries(${PROJECT_NAME} PahoMqttCpp::paho-mqttpp3)
endif()
target_link_libraries(${PROJECT_NAME} Threads::Threads)

