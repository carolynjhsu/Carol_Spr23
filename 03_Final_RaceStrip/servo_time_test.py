from machine import Pin
from time import *
from neopixel import NeoPixel
import unit
from m5stack import *
from servo import Servo
from easyIO import *
from m5mqtt import M5mqtt
import wifiCfg
import car_stopwatch
import car_timer



analog_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
adc = ADC(analog_pin)  # create analog-to-digital converter (ADC) input
adc.atten(ADC.ATTN_11DB)  # set 11dB attenuation (2.45V range)

servo_obj = Servo(Pin(26))  # create a Servo object on G26 (yellow wire)
button_pin = Pin(27, Pin.IN, Pin.PULL_UP) #create button pin 33 , 27 fr atom matrix
button_pushed=0
angle=90
angle_inc=10
minAngle=0
maxAngle=150
type=1
servo_obj = Servo(Pin(26))  # create a Servo object on G26 (yellow wire)


while True:
    if(button_pin.value() == 0):
        car_timer.timer()
        button_pin==1   #servo 
        car_stopwatch.time_convert()
        angle=angle+angle_inc
        if(angle>maxAngle):
            angle_inc=-angle_inc
            if(type==1):
                button_pushed=0
        analog_val = adc.read()  # read
        servo_val = map_value(analog_val, 0, 4095, 1000, angle)
        servo_obj.write_us(servo_val)
        print(servo_val)
        print(angle) 
        sleep_ms(100)