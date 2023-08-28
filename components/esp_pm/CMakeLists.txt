if(IDF_TARGET STREQUAL "linux")
    idf_component_register()
    return()
endif()

idf_component_register(SRCS "pm_locks.c" "pm_trace.c" "pm_impl.c"
                       INCLUDE_DIRS include
                       PRIV_REQUIRES esp_system driver esp_timer
                       LDFRAGMENTS linker.lf)
