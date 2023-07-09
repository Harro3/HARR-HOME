import asyncio
import enum
import discord

class status(enum.Enum):
    IN_PROGRESS = 0x0000ff
    INFO = 0x00ff00
    ERROR = 0xff0000

class Response():
    def __init__(self, ctx, status, message, title):
        self.status_ = status
        self.message_ = message
        self.title_ = title
        self.ctx = ctx

    def status(self, status):
        self.status_ = status
        return self

    def message(self, message):
        self.message_ = message
        return self
    
    def title(self, title):
        self.title_ = title
        return self
    
    def build(self):
        embed = discord.Embed(title=self.status_.name, color=self.status_.value)
        embed.add_field(name=self.title_, value=self.message_, inline=False)
        return embed
    
    async def send(self):
        await self.ctx.edit_original_response(embed=self.build())

    async def send_embed(self, embed):
        await self.ctx.edit_original_response(embed=embed)

async def generate_response(ctx, status=status.IN_PROGRESS, message="action in progress...", title="Message"):
    res = Response(ctx, status, message, title)
    ctx.response.defer()    
    await ctx.response.send_message(embed=res.build())
    return res.status(status.INFO).message("action successful")
