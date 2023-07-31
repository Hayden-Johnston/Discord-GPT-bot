from dotenv import dotenv_values
import discord
from discord.ext import commands
from gptfunctions import chat

config = dotenv_values(".env")

intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix="/", intents=intents)

# ----------------------------- COMMANDS ------------------------------- #

@bot.command()
async def gpt(ctx, arg):
    """Check channel ID and send message to channel"""
    channel = ctx.channel
    if channel.id == 1129457187962499163:
        response = chat(arg)
        await channel.send(response)
    
bot.run(config["DISCORD-TOKEN"])