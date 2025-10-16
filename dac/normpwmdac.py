import RPi.GPIO as GPIO  

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, voltage_range, verbose=False):
        self.gpio_pin = gpio_pin
        self.pwm_freq = pwm_freq
        self.verbose = verbose
        self.voltage_range = voltage_range
        self.pwm = None  

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial=0)
        
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)
        self.pwm.start(0)  

    def deinit(self):
        if self.pwm:
            self.pwm.stop()
        GPIO.cleanup()

    def set_voltage(self, v):
        if not (0.0 <= v <= self.voltage_range):
            print(f"Вне диапазона ({self.voltage_range:.2f}V)")
            print("Установлено 0.0V")
            duty_cycle = 0
        else:
            
            duty_cycle = (v / self.voltage_range) * 100.0
        
        if self.verbose:
            print(f"Установка {v}V -> {duty_cycle:.1f}% заполнения")
        
        self.pwm.ChangeDutyCycle(duty_cycle)  

if __name__ == "__main__":
    try:
        
        dac = PWM_DAC(12, 500, 3.3, True)

        while True:
            try:
                voltage = float(input("Введите напряжение (0-3.3V): "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Ошибка: введите число\n")
    finally:
        dac.deinit()