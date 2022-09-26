from discord.ext import commands
from fractions import *
import discord
import os
import math
from discord import Intents
from keep_online import keep_online

intents = Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def on_ready(ctx):
    await ctx.send(
        "PreCal_Bot Connected! Enter '$instructions' to get started.")


# Instructions - HOW TO USE
@bot.command()
async def instructions(ctx):
    await ctx.send(
        'Follow this link to go to a google doc with instructions on how to use the bot  https://docs.google.com/document/d/1HI1AICdyEXYonJUUFkW0PYfVKGVTT-wbKKEhyqcS9PM/edit?usp=sharing'
    )


@bot.command()
async def pta(ctx, c: int, b: int):
    await ctx.send((c**2 - b**2)**0.5)


@bot.command()
async def ptc(ctx, b: int, a: int):
    await ctx.send((a**2 + b**2)**0.5)


@bot.command()
async def ptb(ctx, c: int, a: int):
    await ctx.send((c**2 - a**2)**0.5)


#Degrees to Radians fuction
pi = ' pi'


@bot.command()
async def rad(ctx, a: int):
    answer = Fraction(a, 180)
    await ctx.send(str(answer) + pi)


# Radians to Degrees
d = ' degrees'


@bot.command()
async def deg(ctx, a: int, b: int = 1):
    answer = Fraction(a * 180, b)
    await ctx.send("{} {}".format(str(answer), d))


#@bot.command()
#async def deg(ctx,a: int,):
# await ctx.send()
#add rad to deg and pie chart


#Pie Chart
@bot.command()
async def pie(ctx):
    await ctx.send(file=discord.File('pie.png'))


@bot.command()
async def special_triangles(ctx):
    await ctx.send(file=discord.File('tri.png'))


@bot.command()
#Token
async def identities(ctx):
    await ctx.send(file=discord.File('i.png'))


token = os.environ.get("Token")
bot.run(token)
my_secret = os.environ['Token']
keep_online()