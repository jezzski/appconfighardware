// App Configurable Hardware: Main (ESP-IDF Framework)
// 11.8.2020: Initializes Flash Storage and Prints "Hello world!" once per second

#include <string.h>
#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_system.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_log.h"
#include "nvs_flash.h"
#include "esp_spi_flash.h"
#include "driver/gpio.h"
#include "sdkconfig.h"

#include "lwip/err.h"
#include "lwip/sys.h"

#define BLINK_GPIO CONFIG_BLINK_GPIO

void app_main()
{
    // Initialize Flash
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
      ESP_ERROR_CHECK(nvs_flash_erase());
      ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);

    while (1) {
        printf("Hello world!\n");
        // Delay 1 second
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
    
}