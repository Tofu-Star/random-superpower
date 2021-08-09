# bot.py
import os
import rand_superpower_code
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='+')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#Go through each of the random category links one by one
#Almighty
@bot.command(name='almighty')
async def roll_almighty(ctx):
    response = rand_superpower_code.randByCategory("almighty")
    await ctx.send(response)

#Constructs
@bot.command(name='construct')
async def roll_construct(ctx):
    response = rand_superpower_code.randByCategory("construct")
    await ctx.send(response)

#Enhancements
@bot.command(name='enhancement')
async def roll_enhancement(ctx):
    response = rand_superpower_code.randByCategory("enhancement")
    await ctx.send(response)

#Magical Powers
@bot.command(name='magical')
async def roll_magical(ctx):
    response = rand_superpower_code.randByCategory("magical")
    await ctx.send(response)

#Manipulations
@bot.command(name='manipulation')
async def roll_manipulation(ctx):
    response = rand_superpower_code.randByCategory("manipulation")
    await ctx.send(response)

#Meta Powers
@bot.command(name='meta')
async def roll_meta(ctx):
    response = rand_superpower_code.randByCategory("meta")
    await ctx.send(response)

#Physiology
@bot.command(name='physiology')
async def roll_physiology(ctx):
    response = rand_superpower_code.randByCategory("physiology")
    await ctx.send(response)

#Psychic Powers
@bot.command(name='psychic')
async def roll_psychic(ctx):
    response = rand_superpower_code.randByCategory("psychic")
    await ctx.send(response)

#Science Powers
@bot.command(name='science')
async def roll_science(ctx):
    response = rand_superpower_code.randByCategory("science")
    await ctx.send(response)

@bot.command(name='superpower')
async def roll_superpower(ctx):
    response = rand_superpower_code.randomSuperpower()
    await ctx.send(response)

#Help statement
@bot.command(name='h')
async def help_response(ctx):
    response = """Thank you for using Random Superpower Bot!\n
In order to roll a truly random superpower, type +superpower.\n
To roll from a specific category, you can type the following:
+almighty for almighty powers.
+construct for constructions.
+enhancement for enhancements.
+magical for magical powers.
+manipulation for manipulations.
+meta for meta powers.
+psychic for psychic powers.
+science for science powers."""
    await ctx.send(response)

bot.run(TOKEN)