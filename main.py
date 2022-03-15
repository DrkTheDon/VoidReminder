#!/usr/bin/python3

#####################################################
## Void Reminder (VoidRD)                          ##
## A discord bot made to remind ppl for events     ##
## https://voidsecurity.ml                         ##
## Coded by: drk, Armez                            ##
#####################################################

# Imports
from ast import arg
from logging import exception
import this
from urllib.parse import uses_fragment
import discord
from colorama import Fore
import time
import os
from datetime import datetime
from discord.ext import commands, tasks
import linecache
import asyncio
import requests
import numpy
from discord.ext.commands import Bot
from discord.utils import get
from discord import Permissions
from discord.ext import *
from discord.ext.commands import bot
from discord.ext.commands.errors import *
from discord.ext.commands.errors import DiscordException, ClientException
import discord.ext.commands.errors
from discord.ext.commands.errors import CommandError, CommandNotFound
import traceback
import sys

## REPLIT IMPORTS
# from replit import db
# from keep_alive import keep_alive

# Global Variabels
TOKEN = "TOKEN"
client = discord.Client()
bot = commands.Bot (command_prefix="*")
bot.remove_command("help")

# Main Defines
@bot.event
async def on_ready():
    print(f"{Fore.MAGENTA}VoidReminder BOT - V.0.2")  
    time.sleep(0.5)
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------{Fore.LIGHTWHITE_EX}")
    print(f"{Fore.GREEN}[+]{Fore.LIGHTWHITE_EX} Conntected to {Fore.YELLOW}{bot.user}")
    print(f"{Fore.YELLOW}[*]{Fore.LIGHTWHITE_EX} Im watching {Fore.YELLOW}{len(bot.guilds)}{Fore.LIGHTWHITE_EX} servers!")
    print(f"{Fore.YELLOW}[!]{Fore.LIGHTWHITE_EX} Send {Fore.GREEN}*help{Fore.LIGHTWHITE_EX} to start!")
    print(f"{Fore.YELLOW}----------------------------------------------------------------------------------{Fore.LIGHTWHITE_EX}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="drk & Armez"))

@bot.command()
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention} PONG!")


@bot.group(invoke_without_command=True)
async def help(ctx):
    embed=discord.Embed(title="VoidReminder Commands", description="""
    `ping` pings the user who send command (tests the bot).
    `remind` setups a remind.
    `about` Sends an about message.
    `credits` list the credits of VoidReminder.
    """, color=0xcc0000)
    embed.set_author(name="drk", url="https://github.com/DrkTheDon", icon_url="https://static.vecteezy.com/system/resources/thumbnails/001/872/742/small/happy-halloween-decoration-design-free-vector.jpg")
    embed.set_footer(text="VoidReminder - 2022")
    await ctx.send(embed=embed)

@bot.command()
async def remind(ctx):
    embed=discord.Embed(title="REMIND", description="""
    `disboard` Reminds when the server can be bumped with the disboard bot.
    `custom` setup a custom remind.
    """, color=0xcc0000)
    embed.set_author(name="drk", url="https://github.com/DrkTheDon", icon_url="https://static.vecteezy.com/system/resources/thumbnails/001/872/742/small/happy-halloween-decoration-design-free-vector.jpg")
    embed.set_footer(text="VoidReminder - 2022")
    await ctx.send(embed=embed)




#  if message == "disboard":
#      await ctx.send(f"{ctx.author.mention} This area is under **construction**!")
#    else:
#        await ctx.send(f"Unknown Remind.")

@bot.command()
async def about(ctx):
    pass

    

@bot.command()
async def credits(ctx):
    await ctx.send(f"**VoidReminder** Is maintained and developed by **drk#6231** (Main Founder) & **Armez#0944** (Co-Founder)")

# keep_alive()
# Help Help cmds

@help.command()
async def remind(ctx):
    embed = discord.Embed(title = "Remind", description = "Sets up a reminder for your server")
    embed.add_field(name = "**How To use**", value = "***remind** <reminder>")
    await ctx.send(embed=embed)

# Main Run
while __name__ == '__main__':
    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Quitting.")
        time.sleep(0.5)
        quit()
    except RuntimeError:
        print(f"{Fore.RED}[-]{Fore.LIGHTWHITE_EX} CTRL + C detected, quitting...")
        time.sleep(0.5)
        quit()
