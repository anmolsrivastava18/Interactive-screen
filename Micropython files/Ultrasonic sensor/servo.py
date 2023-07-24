from machine import Pin, PWM
from time import sleep

class Servo:
    def __init__(self, servo_pin_num):
        self.servo_pin = Pin(servo_pin_num, Pin.IN)
        self.servo = PWM(self.servo_pin)
        self.servo.freq(50)
        # Bring servo to home position
        self.servo.duty(18)
        sleep(1)
    
    def _get_angle(self, duty):       
        self.servo.duty(duty)
        angle = round(36*(duty-18)/19, 2)
        return angle
