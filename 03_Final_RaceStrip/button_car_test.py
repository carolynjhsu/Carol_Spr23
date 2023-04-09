from machine import Pin,ADC
from time import *
import time
from m5stack import *

def countdown(timer):
    while timer:
        min, secs = divmod(timer, 60)
        timeformat = '{:2d}'.format(secs)
        print(timeformat, end='\r')
        sleep_ms(1000)
        timer -= 1
    
    print("Go!")

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  mins = mins % 60
  milli= sec * 1000
  print("LANE 1 = {0}min: {1}sec: {2}ms".format(int(mins),sec,int(milli)))

start_pin=Pin(39, Pin.IN, Pin.PULL_UP)
stop_pin=Pin(33, Pin.IN, Pin.PULL_UP)
program_state="start"


while True: 
    if(program_state=="start"):
        if(start_pin.value()==0):
            countdown(3)
            start_time = time.time()
            program_state="racing"
    elif(program_state=="racing"):
        if(stop_pin.value()==0):
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            program_state="start"
        
