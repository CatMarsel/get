import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(pins, GPIO.OUT)
dynamic_range=3.148

def voltage_to_number(valtage):
    if not (0.0<=voltage<=dynamic_range):
        print(f"Out of range {dynamic_range:.2f}")
        print("Setting 0.0")
        return 0
    return int(voltage / dynamic_range * 255)
def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def num_to_dec(n):
    GPIO.output(pins, dec2bin(n))

try:
    while True:
        try:
            voltage = float(input("Enter the voltage: "))
            num=voltage_to_number(voltage)
            num_to_dec(num)
        
        except ValueError:
            print("You have entered not number  try again\n")
finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()