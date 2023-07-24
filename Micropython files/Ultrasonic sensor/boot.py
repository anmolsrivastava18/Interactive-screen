# This file is executed on every boot (including wake-boot from deepsleep)
# Connect to internet

import network
import esp
import gc
import sys
from time import sleep

esp.osdebug(None)
gc.collect()

ssid = 'JioFiber-S4amp'
password = 'Shiv@1997'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

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
