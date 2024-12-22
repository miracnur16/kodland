import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True # Server Members Intent'i etkinleştirir intents.presences = True # Presence Intent'i etkinleştirir
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yazitura(ctx):
    sayi = random.randint(0,2)
    if sayi == 0:
        await ctx.send("Yazi")
    else:
        await ctx.send("Tura")

bot.run("MTMxNTczMjg5ODQxMzgwNTcwMA.Gj6hnf.xc13tV3mK20_eQRcG3-u2htHxU1mTQtP05_xDg")