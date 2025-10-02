import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        n = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits, n)
        print(n)
    def set_voltage(self, voltage):
        if not (0.0<=voltage<=self.dynamic_range):
            print(f"Out of range {self.dynamic_range:.2f}")
            print("Setting 0.0")
            return 0
        number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)
        print(number)

if __name__ == "__main__":
    try:
        dac=R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.148, True)

        while True:
            try:
                voltage = float(input("Enter the voltage: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("its not number try again\n")
    finally:
        dac.deinit()