import discord
from discord.ext import commands
import random
intents = discord.Intents.all()

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def guess(self, ctx, guess:int):
        number = random.randint(1, 10)
        if guess == number:
            await ctx.send("You guessed it!")
        else:
            await ctx.send("Nope! Better luck next time :)")
    
    @commands.command()
    async def rps(self, ctx, guess:str):
        option = random.choice(["rock", "paper", "scissors"])
        if guess == option:
            await ctx.send("I got " + option + "You won!")
        else:
            await ctx.send("Haha! you chose " + guess + " and I got " + option + ". YOU LOST L + BOZO")

async def setup(bot):
    await bot.add_cog(fun(bot))
