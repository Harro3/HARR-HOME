"""
SenseHat class and SenseEmu hardware implementations.
"""

from hardware import Hardware
import subprocess
from time import sleep

from config import get_config

class SenseHat(Hardware):
    def __init__(self):
        from sense_hat import SenseHat
        self.sense = SenseHat()

    def display_message(self, message):
        color = get_config()["display_text_color"]
        self.sense.show_message(message, text_colour=color)

    def visual_alert(self):
        color = get_config()["visual_alert_color"]
        for i in range (5):
            self.sense.clear(color)
            sleep(0.5)
            self.sense.clear()
            sleep(0.5)


    def get_temperature(self):
        return self.sense.get_temperature()
    
    def get_humidity(self):
        return self.sense.get_humidity()
    
    def get_pressure(self):
        return self.sense.get_pressure()
    
    def get_ip(self):
        ip = str(subprocess.check_output(("hostname", "-i")))
        ip = ip.replace("b", "")
        ip = ip.replace("\\n", "")
        ip = ip.replace("'", "")
        return ip


class SenseEmu(SenseHat):
    def __init__(self):
        from sense_emu import SenseHat
        self.sense = SenseHat()