import discord, os, time
from discord.ext import commands

bot = commands.Bot(command_prefix = "--", self_bot=True)

@bot.event
async def on_ready():
    print("Linux Kyrios Bumper is Online!")

@bot.command()
async def bump(ctx):
    while True:
        await ctx.send("!d bump")
        print("Bump sent")
        time.sleep(7200)

token = "Nzc3NDc4ODQ1ODc5NTQ5OTUy.YMOw9w.et1U9tLErliZL4Xi70vvmzmsDZI"

bot.run(token, bot = False)
