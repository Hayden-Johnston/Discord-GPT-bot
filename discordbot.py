import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from gptfunctions import chat

if os.path.exists(".env") == True:
    load_dotenv()
discord_token = os.environ["DISCORD-TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix="/", intents=intents)

# ----------------------------- COMMANDS ------------------------------- #

@bot.command()
async def gpt(ctx):
    """Check channel ID and send message to channel"""
    channel = ctx.channel
    content = ctx.message.content
    if channel.id == 1129457187962499163:
        response = chat(content)
        await channel.send(response)
    
bot.run(discord_token)