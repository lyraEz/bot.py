import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=',', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Testing%"))
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello Discord!")

bot.run('Token')
