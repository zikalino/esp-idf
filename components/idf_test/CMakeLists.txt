if(IDF_TARGET STREQUAL "linux")
    idf_component_register()
    return()
endif()

idf_build_get_property(target IDF_TARGET)

idf_component_register(INCLUDE_DIRS "include" "include/${target}")
