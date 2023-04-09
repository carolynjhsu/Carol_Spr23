import time

def countdown(timer):
    while timer:
        min, secs = divmod(timer, 60)
        timeformat = '{:2d}'.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timer -= 1
        
    print("Go!")
(countdown(3))