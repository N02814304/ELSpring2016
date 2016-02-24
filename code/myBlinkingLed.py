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

