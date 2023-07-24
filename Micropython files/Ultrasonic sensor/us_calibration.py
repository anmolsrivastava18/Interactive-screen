from ultrasonic import Ultrasonic
from time import sleep
from servo import Servo

servo = Servo(servo_pin_num=26) # To bring the servo on home position
us_sensor = Ultrasonic(trigger_pin=13, echo_pin=14, echo_timeout_us=10000)
log = open("log.txt" , "a")

while True:
    distance = us_sensor.distance_cm()
    print(distance)
    log.write(f"{distance}\n")
    sleep(1)
