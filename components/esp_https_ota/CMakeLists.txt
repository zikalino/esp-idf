if(IDF_TARGET STREQUAL "linux")
    idf_component_register()
    return()
endif()

idf_component_register(SRCS "src/esp_https_ota.c"
                    INCLUDE_DIRS "include"
                    REQUIRES esp_http_client bootloader_support esp_app_format esp_event
                    PRIV_REQUIRES log app_update)
