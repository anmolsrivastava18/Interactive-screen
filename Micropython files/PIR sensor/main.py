from machine import Pin
from time import sleep, localtime, time

pir1 = Pin(0, Pin.IN)
pir2 = Pin(2, Pin.IN)
pir3 = Pin(4, Pin.IN)

log = open("log.txt" , "a")

def padding(string):
    if len(string) < 2:
        return "0" + string
    return string

def printLog(time_tuple, value1, value2, value3):
    dd = padding(str(time_tuple[2]))
    mm = padding(str(time_tuple[1]))
    yyyy = padding(str(time_tuple[0]))
    hrs = padding(str(time_tuple[3]))
    mins = padding(str(time_tuple[4]))
    sec = padding(str(time_tuple[5]))
    date = f"{dd}-{mm}-{yyyy}"
    time = f"{hrs}:{mins}:{sec}"
    timestamp = date + " " + time
    print(timestamp)
    log.write(f"{timestamp}; {value1}; {value2}; {value3}\n")
#     sleep(1)

print("Ready to detect...")

while True:
    if pir1.value() or pir2.value() or pir3.value():
        printLog(localtime(time()), pir1.value(), pir2.value(), pir3.value())
