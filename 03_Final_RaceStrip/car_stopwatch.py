import time

'''
import machine
import time
photo_pin = machine.ADC(26)

while True:
    val = photo_pin.read_u16()
    print(val)
    time.sleep(.2)'''

def time_convert(sec):
  mins = sec // 60
  sec = sec / 60
  mins = mins % 60
  millis = sec % 1000
  print("LANE 1 = {0}:{1}:{2}".format(int(mins),int(sec),millis))
input("Press Enter to start")
start_time = time.time()
input("Press enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
