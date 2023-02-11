from m5stack import *
from machine import Pin,PWM

led_pin = Pin(32, Pin.OUT)    
led_pin_02 = Pin(25, Pin.OUT)
light=machine.PWM(led_pin, freq=600)
led_pwm=machine.PWM(led_pin_02, freq=20)
button_pin_01 = Pin(26, Pin.IN, Pin.PULL_UP)  # create pull-up input on pin G26 (yellow wire)  
button_pin_02 = Pin(21, Pin.IN, Pin.PULL_DOWN)
State=0

while True:
    if (button_pin_02.value()== 0):
        led_pwm.init()
        for i in range(100):
            led_pwm.duty(i)
        for i in range(100):
            led_pwm.duty(100-i)
            wait_ms(1)
        else:
            led_pwm.deinit()
            light.deinit()
    if (button_pin_01.value() == 0):       #key press
        light.init()
        wait_ms(100)
        for i in range(100):
            light.duty(i)  
    else:
        light.deinit()
        wait_ms(50)
