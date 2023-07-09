"""
SenseHat class and SenseEmu hardware implementations.
"""

from hardware import Hardware

class SenseHat(Hardware):
    def __init__(self):
        from sense_hat import SenseHat
        self.sense = SenseHat()

    def display_message(self, message):
        self.sense.show_message(message)

    def get_temperature(self):
        return self.sense.get_temperature()
    
    def get_humidity(self):
        return self.sense.get_humidity()
    
    def get_pressure(self):
        return self.sense.get_pressure()

class SenseEmu(SenseHat):
    def __init__(self):
        from sense_emu import SenseHat
        self.sense = SenseHat()