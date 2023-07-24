# This file is executed on every boot (including wake-boot from deepsleep)
# Connect to internet

import network
import esp
import gc
import sys
from time import sleep

esp.osdebug(None)
gc.collect()

# Replace these with your Wi-Fi credentials
SSID = 'WiFi@Home'
PASSWORD = 'C@tchmeifUcan'

# Set up Wi-Fi connection
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(SSID, PASSWORD)

print("Connecting", end="")
sleep_counter = 0
while station.isconnected() == False:
    print(".", end="")
    if sleep_counter <= 40:
        sleep_counter += 1
    else:
        print("\n\nTaking too much time to connect to the network! Aborting now")
        sys.exit()
    sleep(0.25)

print('\nConnection successful')
print(station.ifconfig())
