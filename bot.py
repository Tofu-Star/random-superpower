# bot.py
import os
from discord import guild
from discord.flags import Intents
import rand_superpower_code
import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intent = discord.Intents.default()
bot = commands.Bot(command_prefix='+', Intents = intent)
slash = SlashCommand(bot, sync_commands=True)

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@slash.slash(name="Superpower", 
description="Roll a random superpower!")
async def superpower(ctx):
    response = rand_superpower_code.randomSuperpower()
    await ctx.send(response)

@bot.command(name='superpower')
async def roll_superpower(ctx, category = None):
    category = category.lower().strip()

    response = rand_superpower_code.randomSuperpower(category=category)

    await ctx.send(response)

#Help statement
@bot.command(name='h')
async def help_response(ctx):
    response = """Thank you for using Random Superpower Bot!\n
In order to roll a truly random superpower, type +superpower.\n
To roll from a specific category, you can type the following after +superpower:
'almighty' for almighty powers.
'construct' for constructions.
'enhancement' for enhancements.
'magical' for magical powers.
'manipulation' for manipulations.
'meta' for meta powers.
'physiology' for physiologies
'psychic' for psychic powers.
'science' for science powers."""
    await ctx.send(response)

bot.run(TOKEN)