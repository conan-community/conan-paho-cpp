if(PahoMqttC_FOUND)
    return()
endif()

find_path(PahoMqttC_INCLUDE_DIR NAMES MQTTClient.h PATHS "${CONAN_INCLUDE_DIRS_PAHO-C}")
find_library(PahoMqttC_LIBRARY NAMES ${CONAN_LIBS_PahoMqttC} PATHS "${CONAN_LIB_DIRS_PAHO-C}")

set(PahoMqttC_FOUND TRUE)
set(PahoMqttC_INCLUDE_DIRS ${PahoMqttC_INCLUDE_DIR})
set(PahoMqttC_LIBRARIES ${CONAN_LIBS_PAHO-C})
mark_as_advanced(PahoMqttC_LIBRARIES PahoMqttC_LIBRARY PahoMqttC_INCLUDE_DIR)

if (NOT TARGET PahoMqttC::PahoMqttC)
    add_library(PahoMqttC::PahoMqttC INTERFACE IMPORTED)
    set_target_properties(PahoMqttC::PahoMqttC PROPERTIES
        INTERFACE_INCLUDE_DIRECTORIES "${PahoMqttC_INCLUDE_DIR}"
        INTERFACE_LINK_LIBRARIES "${PahoMqttC_LIBRARIES}"
    )
endif()