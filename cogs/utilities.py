import discord
import random
from discord.ext import commands


class utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
'''insert
- mute
- ban
- warn
- kick commands
'''

async def setup(bot):
    await bot.add_cog(utilites(bot))
