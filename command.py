import discord
from discord.ext import commands

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("command cog functional")

    @commands.command()
    async def repo(self, ctx):
         await ctx.send("https://github.com/gamerchill/testbot/blob/main/discord%20code") # calls this repository

    @commands.command()
    async def hello(self, ctx):
         await ctx.reply("This command is useless. for now :)") #soon to be changed

    @commands.command()
    async def needhelp(self, ctx):
         await ctx.reply("Why does @bot.command and @bot.event not work together if put together?\nCommands: .ping\n.repo\n.needhelp") #test command

    @commands.command()
    async def say(self, ctx, *, arg):
      await ctx.send(arg) #repeats what user says

    @commands.command() #this whole function sends an embed with values
    async def embed(self, ctx, member:discord.Member = None):
     if member == None:
        member = ctx.author

        name = member.display_name
        pfp = member.display_avatar

        embed = discord.Embed(title = "This is a title", description = "this is a description", color=discord.Color.random())
        embed.set_author(name=f"{name}")
        embed.set_thumbnail(url=f"{pfp}")
        embed.add_field(name = "this is field 1", value ="this is a field")
        embed.add_field(name="this is another field", value = "this field inline is true", inline=True)
        embed.add_field(name="this is field 3", value = "this inline is false", inline=False)
        embed.set_footer(text=f"{name} set this embed!")

     await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(command(bot))
