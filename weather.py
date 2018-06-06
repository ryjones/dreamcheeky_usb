#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from time import sleep, strftime
import os
from dcusb import driver

# Get openweathermap.org API key and ZIP code from env var
API_KEY = os.environ['OWM_API_KEY']
ZIP_CODE = os.environ['ZIP_CODE']


def main():
    try:
        leds = driver.LEDMessageBoard()
    except Exception as e:
        print(f'Unable to open LED Message Board: {e}')

    while True:
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE},us&appid={API_KEY}"
        response = requests.post(url).json()

        current_temp = round(1.8 * (response['main']['temp'] - 273) + 32, 1)

        leds.clear_screen()
        leds.scroll_message("Current Temp:", 21, 60)

        leds.write_string(f"{current_temp}ºF", 0)
        for _ in range(50):
            leds.push_screen()
            sleep(.1)

        sleep(.5)

        leds.clear_screen()
        leds.scroll_message("Current Time:", 21, 60)

        leds.write_string(f"{strftime('%H:%M')}", 1)
        for _ in range(50):
            leds.push_screen()
            sleep(.1)

        sleep(.5)


if __name__ == "__main__":
    main()
