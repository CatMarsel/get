import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_f, dr, verbose=False):
        self.gpio_pin=gpio_pin
        self.pwm_f=pwm_f
        self.verbose=verbose
        self.dr = dr

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    
    def set_voltage(self, v):
        if not (0.0<=voltage<=self.dr):
            print(f"Out of range {self.dr:.2f}")
            print("Setting 0.0")
            return 0
        d=self.dr/100.0
        pwm=GPIO.PWM(self.gpio_pin, self.pwm_f)
        a=v/d
        pwm.start(a)


if __name__ == "__main__":
    dac = PWM_DAC(12, 500, 3.290, True)
    try:
        

        while True:
            try:
                voltage=float(input("Enter the voltage: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Its not number try again\n")
    finally:
        dac.deinit()