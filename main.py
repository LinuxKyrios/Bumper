import discord, os, time
from discord.ext import commands

bot = commands.Bot(command_prefix = "--", self_bot=True)

@bot.event
async def on_ready():
    print("Linux Kyrios Bumper is Online!")

@bot.command()
async def bumper(ctx):
    while True:
        await ctx.send("!d bump")
        time.sleep(7260)

token = "Nzc3NDc4ODQ1ODc5NTQ5OTUy.YMOo2g.4SfjBkr-VYULAkfZ8senkUSL690"

bot.run(token, bot = False)