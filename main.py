import discord, os, time
from discord.ext import commands

#setting prefix for script
bot = commands.Bot(command_prefix = "--", self_bot=True)

#Console confirmation that script is working
@bot.event
async def on_ready():
    print("Linux Kyrios Bumper is OnLine!")

#Command to execute on discord
@bot.command()
async def bump(ctx):
    while True:
        await ctx.send("!d bump")
        print("Bump sent")
        time.sleep(7200)

#token is necessary to connect with accounton discord
token = "Nzc3NDc4ODQ1ODc5NTQ5OTUy.YMRMBQ.s37MyzIMGuV_jsAcCg7pC7Dscm8"

#execute the script
bot.run(token, bot = False)
