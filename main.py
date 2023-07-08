import os
from dotenv import load_dotenv

from discord_bot import client

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client.run(DISCORD_TOKEN)