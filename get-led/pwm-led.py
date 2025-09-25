import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

pwm=GPIO.PWM(led, 200)
d=0.0
pwm.start(d)
while True:
    pwm.ChangeDutyCycle(d)
    time.sleep(0.05)
    d+=1.0
    if d>100.0:
        d=0.0