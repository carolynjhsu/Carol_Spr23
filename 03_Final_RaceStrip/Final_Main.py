from machine import Pin,ADC
from time import *
from m5stack import *
# from servo_time_test import *
from servo import Servo

rgb.set_screen([0,0,0,0,0,0,0x00ff00,0x00ff00,0x00ff00,0,0,0x00ff00,0,0x00ff00,0,0,0x00ff00,0x00ff00,0x00ff00,0,0,0,0,0,0])
def countdown(timer):
    while timer:
        min, secs = divmod(timer, 60)
        timeformat = '{:2d}'.format(secs)
        print(timeformat)
        sleep_ms(1000)
        timer -= 1
    print("Go!")


def time_convert(mill):
    sec = mill/1000
    return sec
    # mins = sec // 60
    # sec = sec // 60
    # mins = mins % 60
    # millis = sec*1000
    # print("{0}:{1}".format(sec,int(millis)))

start_pin=Pin(39, Pin.IN, Pin.PULL_UP)
lane_1_stop=Pin(33, Pin.IN, Pin.PULL_UP)
lane_2_stop=Pin(23, Pin.IN, Pin.PULL_UP)

program_state="start"
lane1_finished = False
lane2_finished = False


sensor1 = ADC(Pin(33)) 
# analog-to-digital converter (ADC) input on pin G33
sensor1.atten(ADC.ATTN_11DB) # adjust adc1 sensitivity
sensor2 = ADC(Pin(32)) 
# analog-to-digital converter (ADC) input on pin G32
sensor2.atten(ADC.ATTN_11DB) # adjust adc2 sensitivity

button_timer=0

print("compiled")

while True: 
    # print(program_state)
    if(program_state=="start"):
        if(start_pin.value()==0):
            countdown(3)
            start_time_1 = ticks_ms()
            start_time_2 = ticks_ms()
            servo_obj = Servo(Pin(26))  # create a Servo object on G26 (yellow wire)
            servo_obj.write_angle(100)
            sleep_ms(500)
            servo_obj.write_angle(9)
            print("servo")
            program_state="racing"
    if(program_state=="racing"):
        # print("Start racing")
        lane_val1 = sensor1.read() #start reading values for sensor to prepare for race end
        lane_val2 = sensor2.read()
        print(lane_val2)
        if(lane_val1<1500):
            end_time_1 = ticks_ms()
            lane1_finished = True
        elif(lane_val2<1500):
            end_time_2 = ticks_ms()
            lane2_finished = True
            # print("lane 2")
        if (lane1_finished and lane2_finished):
            program_state="END GAME"
    if(program_state=="END GAME"):
        time_lapsed_1 = end_time_1 - start_time_1
        time_lapsed_2 = end_time_2 - start_time_2
        if(time_lapsed_1<time_lapsed_2):
            print("LANE 1 WINS:",time_convert(time_lapsed_1))
            print("LANE 2:",time_convert(time_lapsed_2))
        else:
            print("LANE 2 WINS:",time_convert(time_lapsed_2))
            print("LANE 1:",time_convert(time_lapsed_1))
        program_state="start"
