from machine import Pin
from time import *
from neopixel import NeoPixel
import unit
from m5stack import *

state=0
tof_sensor = unit.get(unit.TOF, unit.PORTA)
rainbow = [
  (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
  (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
  (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
  (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]

neopixel_pin = Pin(23, Pin.OUT)  # configure output on pin G26 (yellow wire) ##change pin from 26 to 27 which is atom matrix display, in order to fill atom screen in stead of neopixel
neopixel_strip = NeoPixel(neopixel_pin, 30)  # create NeoPixel object with 30 pixels

def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min): 
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

while True:
    d = tof_sensor.distance  # get distance from ToF sensor, right now it's reading the sensor but not well 
    brightness=map_value(d,0,4000, out_min = 0, out_max = 255)
    print(brightness)
    for pixel_index in range(30):
        if(pixel_index<brightness): 
            neopixel_strip[pixel_index] = (100,0,100)
            neopixel_strip.write()
        elif(brightness>0 and brightness<=3):
            for i in range(30):
                rainbow = rainbow[-i:] + rainbow[:-i]
                neopixel_strip[i] = rainbow[pixel_index]
                neopixel_strip.write()
                sleep_ms(40)
        else:
            print(brightness)
            neopixel_strip[pixel_index]=(200,0,0)
            neopixel_strip.write()
            