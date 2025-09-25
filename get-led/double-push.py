import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds=[16,12,25,17,27,23,22,24]
up=9
dw=10
st=0.2
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(up,GPIO.IN)
GPIO.setup(dw, GPIO.IN)

GPIO.output(leds, 0)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(dw) and GPIO.input(up):
        num=255
    elif GPIO.input(dw):
        num=num-1
        if num>=256 or num<0:
            num=0
        print(num, dec2bin(num))
        time.sleep(st)

    elif GPIO.input(up):
        num=num+1
        if num>=256 or num<0:
            num=0
        print(num, dec2bin(num))
        time.sleep(st)

    if num>=256 or num<0:
        num=0
    GPIO.output(leds, dec2bin(num))