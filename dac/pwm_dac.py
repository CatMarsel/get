import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_f, dr, verbose=False):
        self.gpio_pin=gpio_pin
        self.pwm_f=pwm_f
        self.verbose=verbose
        self.dr = dr

        self.pwm=None

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

        self.pwm=GPIO.PWM(self.gpio_pin, self.pwm_f)
        self.pwm.start(0)
        
    
    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()
    
    def set_voltage(self, v):
        if not (0.0<=v<=self.dr):
            print(f"Out of range {self.dr:.2f}")
            print("Setting 0.0")
            return 0
        else:
            
            print((v/self.dr)*100.0)

            self.pwm.ChangeDutyCycle((v/self.dr)*100.0)


if __name__ == "__main__":
    
    try:
        dac = PWM_DAC(12, 500, 3.148, True)

        while True:
            try:
                voltage=float(input("Enter the voltage: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Its not number try again\n")
    finally:
        dac.deinit()