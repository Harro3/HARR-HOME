import discord
from discord import app_commands

import hardware as sh
import response as rsp


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client=client)


@tree.command(name = "display_message", description = "Show a message on the Sense Hat")
async def display_message(ctx, message:str):
    await rsp.respond(ctx, "Message displaying...", rsp.status.SUCCESS)
    sh.display_message(message)

@client.event
async def on_ready():
    await tree.sync()
    print("Bot is ready!")
