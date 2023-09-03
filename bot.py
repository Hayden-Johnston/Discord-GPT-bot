# author: Hayden Johnston
# date: 08/20/2023
# description: Discord bot for GPT-3 chatbot

import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from app import chat

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
    user_id = ctx.message.author.id
    if channel.id == 1129457187962499163:
        response = chat(content, user_id)
        await channel.send(response)

# ----------------------------- FUNCTIONS ------------------------------ #

def run():
    """Start function"""
    bot.run(discord_token)
