import RPi.GPIO as GPIO
from time import sleep
import time
b1=40
b2=38
LED=37
DC=50
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
myPWM=GPIO.PWM(LED,100)
myPWM.start(DC)
try:
        while True:
                if GPIO.LOW==GPIO.input(b1):
                        if DC<99:
                                DC=min(99,DC+1)
                                myPWM.ChangeDutyCycle(DC)
                                time.sleep(0.05)
                        if DC==99:
                                print('max')
                elif GPIO.LOW==GPIO.input(b2):
                        if DC>0:
                                DC=max(0,DC-1)
                                myPWM.ChangeDutyCycle(DC)
                                time.sleep(0.03)
                        if DC==0:
                                print('min')
                elif GPIO.input(b1)==GPIO.HIGH and GPIO.input(b2)==GPIO.HIGH:
                        time.sleep(0.01)
except KeyboardInterrupt:
        myPWM.stop()
        GPIO.cleanup()
