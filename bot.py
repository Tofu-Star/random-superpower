# bot.py
import os
import rand_superpower_code
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='superpower')
async def roll_superpower(ctx):
    response = rand_superpower_code.randomSuperpower()
    await ctx.send(response)

bot.run(TOKEN)