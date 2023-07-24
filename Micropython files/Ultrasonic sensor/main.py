from time import sleep, localtime, time
from servo import Servo
from ultrasonic import Ultrasonic

servo = Servo(servo_pin_num=26)
us_sensor = Ultrasonic(trigger_pin=13, echo_pin=14, echo_timeout_us=10000)

log = open("log.txt" , "a")

def padding(string):
    if len(string) < 2:
        return "0" + string
    return string

def printLog(time_tuple, angle, distance):
    dd = padding(str(time_tuple[2]))
    mm = padding(str(time_tuple[1]))
    yyyy = padding(str(time_tuple[0]))
    hrs = padding(str(time_tuple[3]))
    mins = padding(str(time_tuple[4]))
    sec = padding(str(time_tuple[5]))
    date = f"{dd}-{mm}-{yyyy}"
    time = f"{hrs}:{mins}:{sec}"
    timestamp = date + " " + time
    print(f"{timestamp}; {angle}; {distance}")
    log.write(f"{timestamp};{angle};{distance}\n")

while True:
    for d in range(18,114,1):
        angle = servo._get_angle(d)
        distance = us_sensor.distance_cm()
        printLog(localtime(time()), angle, distance)
        sleep(0.1)
        
    sleep(0.1)

    for d in range(113,17,-1):
        angle = servo._get_angle(d)
        distance = us_sensor.distance_cm()
        printLog(localtime(time()), angle, distance)
        sleep(0.1)
