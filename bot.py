import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Бот запускается...")


@client.command(aliases=["перегруз"])
async def reload(ctx, extension):
    if ctx.author.id == 607618056537112657:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send("Cogs перезагружается...")
        client.load_extension(f"cogs.{extension}")
        await ctx.send("Cogs готов к использованию!")
    else:
        await ctx.send("You not a dev!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


# connect
token = open("D:\\Project\\bot_discord\\server\\token.txt", "r").readline()
client.run(token)
