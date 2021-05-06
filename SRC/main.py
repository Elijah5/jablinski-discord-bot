#---Imports---#
import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import json
import os
import re
import time
import discord.utils

#---Prefix Dict---#
defaultPrefix = '>'
prefixDict = {}


#---Get Prefix---#
async def get_pre(bot, message):
    ###Create a dict entry if there isnt one###
    if len(prefixDict) > 0:
        guildID = str(next(iter(prefixDict)))
        return prefixDict[guildID]

        try:
            dictRead = open("prefixDict.json", "r")
            dictRead.read(dictFile)
            print(guildID + "This Guild already has an entry")
            dictRead.close()

        except:
            dictRead = open("prefixDict.json", "r")
            dictRead.read(dictFile)
            dictRead.close()
            print("This Guild has no entry... Appending the default prefix")
            dictWrite = open("prefixDict.json", "w")
            dictWrite.write(dictFile)

            dictWrite.close()

###If there is no server set prefix, return defaultPrefix###
    else:
        return [defaultPrefix]


#---Discord.py Def---#
bot = commands.Bot(command_prefix=get_pre)


#---Print When Ready---#
@bot.event
async def on_ready():
    print("-----------------------------------------------")
    print("Bot Is Online!")
    print("-----------------------------------------------")
    await bot.change_presence(activity=discord.Game(name='>help'))


#---Cog Setup---#
@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id == (
            420437587413434369) or ctx.message.author.id == (
                547092292121657344):
        bot.load_extension(f'cogs.{extension}')
        await ctx.send("Cog `" + extension + "` Loaded!")
    else:
        ctx.send("You are not authorized to control Cogs!")


###Unload###
@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id == (
            420437587413434369) or ctx.message.author.id == (
                547092292121657344):
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send("Cog `" + extension + "` Unloaded!")
    else:
        ctx.send("You are not authorized to control Cogs!")


###Reload###
@bot.command()
async def reload(ctx, extension):
    if ctx.message.author.id == (
            420437587413434369) or ctx.message.author.id == (
                547092292121657344):
        bot.unload_extension(f'cogs.{extension}')
        time.sleep(0.3)
        bot.load_extension(f'cogs.{extension}')
        await ctx.send("Cog `" + extension + "` Reloaded!")
    else:
        ctx.send("You are not authorized to control Cogs!")


###Load The Files###
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


#---Ping delay test---#
@bot.command()
async def ping(ctx):
    latency = (bot.latency)
    msLatency = latency * 1000
    strLatency = str(msLatency)
    roundLatency = strLatency[0:5]
    await ctx.send("Pong! `(" + roundLatency + " ms)`")


#---Set Prefix---#
@bot.command()
@has_permissions(administrator=True)
async def prefix(ctx, prefix):
    if len(prefix) > 3:
        await ctx.send(
            "Usage: \n ```>prefix <prefix> \n Note: prefix can take 3 characters only.```"
        )
    else:
        setPrefix = prefix
        guildID = str(ctx.guild.id)
        prefixDict[guildID] = [setPrefix, defaultPrefix]
        await ctx.send("Prefix set to `" + setPrefix + ("` \n `") + setPrefix +
                       ("help`"))

        dictFile = json.dumps(prefixDict)
        f = open("prefixDict.json", "w")
        f.write(dictFile)
        f.close()


#---Stop Bot Command---#
@bot.command()
async def stop(ctx):
    ###Only Allow Authorized Users to Stop the Bot###
    if ctx.message.author.id == (
            420437587413434369) or ctx.message.author.id == (
                547092292121657344):
        await ctx.send("Stopping!")
        exit()
    ###If Not Authorized, Let Them Know!###
    else:
        await ctx.send("You are not authorized to use stop!")


#---Discord Bot API Token---#
bot.run("NjI2NDY1NzE5MjMxNDQ3MDQw.XYufqg.d9oD33BRGsWNcwtdnE1aKBs8mYY")