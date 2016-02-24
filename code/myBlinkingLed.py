# I used 2 separate for loops for each set of blinks. The first three blinks occur in the first for loop while the next four blinks occur in the next.
# Since the whole thing is in a while(true) loop, it will keep repeating the cycle until the user enters CTRL+C. 
# Each blink is separated by half a second, while each set of blinks is separated by 5 seconds. 

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
def Blink():
    while(True):
       for i in range(0,3):
          print "blink #" + str(i + 1)
          GPIO.output(17,True)
          time.sleep(0.5)
          GPIO.output(17,False)
          time.sleep(0.5)
       print "Next phase in 5 seconds"
       time.sleep(5)
       for x in range(0,4):
         print "blink #" + str(x + 4)
         GPIO.output(17,True)
         time.sleep(0.5)
         GPIO.output(17,False)
         time.sleep(0.5)
       print "repeating in 5 seconds"
       time.sleep(5)
    print "done!!"
    GPIO.cleanup()
Blink()

