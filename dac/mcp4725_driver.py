import smbus
import RPi.GPIO as GPIO

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
    
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
    
        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разраядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, v):
        n = [int(bit) for bit in bin(v)[2:].zfill(8)]
        self.set_number(n)

if __name__ == "__main__":
    try:
        dac=MCP4725(3.3)

        while True:
            try:
                voltage = float(input("Enter the voltage: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("its not number try again\n")
    finally:
        dac.deinit()