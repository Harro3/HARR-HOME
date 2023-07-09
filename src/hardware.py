"""
This is the hardware default object. It has to be implemented in the hardware.py file.
The default Hardware implementation is for the CLI."""

class Hardware():
    def __init__(self):
        pass

    def display_message(self, message):
        print(message)

    def get_temperature(self):
        return 0
    
    def get_humidity(self):
        return 0
    
    def get_pressure(self):
        return 0


hardware = Hardware()

def get_hardware():
    return hardware

def set_hardware(hardware_impl):
    global hardware
    hardware = hardware_impl