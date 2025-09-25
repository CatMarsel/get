import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

led = 26

f = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(f, GPIO.IN)

while True:
    GPIO.output(led, not(GPIO.input(f)))