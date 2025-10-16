import smbus
import RPi.GPIO as GPIO

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return

        # Формируем данные для отправки
        first_byte = (number >> 8) & 0x0F  # Старшие 4 бита
        second_byte = number & 0xFF         # Младшие 8 битов
        
        # Отправляем данные по I2C
        self.bus.write_i2c_block_data(self.address, first_byte, [second_byte])

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{first_byte:02X}, 0x{second_byte:02X}]")
    
    def set_voltage(self, v):
        # Преобразуем напряжение в цифровое значение
        if v < 0:
            v = 0
        elif v > self.dynamic_range:
            v = self.dynamic_range
            
        n = int((v / self.dynamic_range) * 4095)
        self.set_number(n)

if __name__ == "__main__":
    try:
        dac = MCP4725(3.3)

        while True:
            try:
                voltage = float(input("Enter the voltage: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("It's not a number, try again\n")
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        dac.deinit()