import os
from dotenv import load_dotenv

from discord_bot import client
from hardware import set_hardware
from src.sense_hardware import SenseHat, SenseEmu


load_dotenv()

if os.getenv("HARDWARE") == "sensehat":
    set_hardware(SenseHat())
elif os.getenv("HARDWARE") == "senseemu":
    set_hardware(SenseEmu())

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


client.run(DISCORD_TOKEN)