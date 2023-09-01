import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping cog online")

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"pong! {round(self.bot.latency* 1000)} ms")

async def setup(bot):
    await bot.add_cog(Ping(bot))
