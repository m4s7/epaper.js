{
    "targets": [
        {
            "target_name": "waveshare9in7",
            "cflags!": [
                "-fno-exceptions",
                "-Wextra"
            ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "sources": [ 
                "./src/c/bcm2835.c",
                "./src/c/DEV_Config.c",
                "./src/c/dev_hardware_SPI.c",
                "./src/c/EPD_9in7.c",
                "./src/c/RPI_sysfs_gpio.c"
            ],
            "defines": [
                "RPI",
                "USE_DEV_LIB"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "libraries": [
                "-lm"
            ]
        }
    ]
}
