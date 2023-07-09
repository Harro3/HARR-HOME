"""
This file contains the discord client and sets up the slash commands.
"""

import discord
from discord import app_commands

from hardware import get_hardware
from response import generate_response, status
import config as cfg

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)

def is_owner(ctx):
    return ctx.user.id == cfg.get_config()["owner_id"]


@tree.command(name = "display_message", description = "Show a message on the Sense Hat")
async def display_message(ctx, message:str):
    res = await generate_response(ctx)
    get_hardware().display_message(message)
    await res.message(f"Displayed message: {message}").send()


@tree.command(name = "get_config", description = "Display the current config")
async def get_config(ctx):
    res = await generate_response(ctx)
    embed = discord.Embed(title="CONFIG", color=0x00ff00)
    for key, value in cfg.get_config(True).items():
        embed.add_field(name=key, value=value, inline=False)
    await res.send_embed(embed)


@tree.command(name = "update_config", description = "Set a config parameter (has to be valid json)")
async def update_config(ctx, parameter:str, value:str):
    res = await generate_response(ctx)
    if not is_owner(ctx):
        res.message("You are not the owner of this bot!").status(status.ERROR)
    elif not cfg.set_config(parameter, value):
        res.message(f"Parameter does not exist or value is not valid").status(status.ERROR)
    else:
        res.message(f"Set {parameter} to {value}")
    await res.send()

@tree.command(name = "get_temperature", description = "Get the current temperature of the hardware")
async def get_temperature(ctx):
    res = await generate_response(ctx)
    await res.title("Current temperature").message(f"{get_hardware().get_temperature()} celsius").send()

@tree.command(name = "get_humidity", description = "Get the current humidity of the hardware")
async def get_humidity(ctx):
    res = await generate_response(ctx)
    await res.title("Current humidity").message(f"{get_hardware().get_humidity()} %").send()

@tree.command(name = "get_pressure", description = "Get the current pressure of the hardware")
async def get_pressure(ctx):
    res = await generate_response(ctx)
    await res.title("Current pressure").message(f"{get_hardware().get_pressure()} millibar").send()


@tree.command(name = "get_ip", description = "Get the current IP of the hardware")
async def get_ip(ctx):
    res = await generate_response(ctx)
    await res.title("Current IP").message(f"{get_hardware().get_ip()}").send()

@tree.command(name = "visual_alert", description = "Trigger a visual alert on the hardware")
async def visual_alert(ctx):
    res = await generate_response(ctx)
    get_hardware().visual_alert()
    await res.message(f"Visual alert triggered").send()

@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user} has connected to Discord!")
