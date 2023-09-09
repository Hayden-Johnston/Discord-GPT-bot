# author: Hayden Johnston
# date: 09/07/2023
# description: Discord bot for GPT-3 chatbot

import discord, os
from discord.ext import commands
from dotenv import load_dotenv
from app import chat, handle_memory
from db import get_by_id, delete_memory

if os.path.exists(".env") == True:
    load_dotenv()
discord_token = os.environ["DISCORDTOKEN"]

intents = discord.Intents.default()
intents.message_content = True
bot=commands.Bot(command_prefix="/", intents=intents)

# ----------------------------- COMMANDS ------------------------------- #
# data saved as string separated by ", " - [{"role": "system", "content": "You are an AI assisstant that only responds in 400 or less characters without commas."}, {"role": "user", "content": "Hello World"}}]
@bot.command()
async def gpt(ctx):
    """Query GPT-3 from chat-gpt channel"""
    channel = ctx.channel
    content = ctx.message.content
    user_id = ctx.message.author.id
    if channel.id == 1129457187962499163:
        if len(content) > 400:
            response = "Error: character limit (400) exceeded."
        else:
            user_memory = get_by_id(user_id)

            if user_memory == []:
                data = [
                    {"role": "system", "content": "You are an AI assisstant that only responds in 400 or less characters without commas."},
                    {"role": "user", "content": content[5:]}
                ]
                response = chat(data)
                handle_memory(user_id, content[5:], response)

            else:
                user_memory = user_memory[0][1].split(", ")
                
                data = [
                    {"role": "system", "content": "You are an AI assisstant that only responds in 400 or less characters without commas."},
                    {"role": "user", "content": user_memory[0]},
                    {"role": "system", "content": user_memory[1]},
                    {"role": "user", "content": user_memory[2]},
                    {"role": "system", "content": user_memory[3]},
                    {"role": "user", "content": content[5:]}
                ]
                response = chat(data)
                handle_memory(user_id, content[5:], response)

        await channel.send(response)

@bot.command()
async def dgpt(ctx):
    """Get more detailed response, not using chat memory"""
    channel = ctx.channel
    content = ctx.message.content
    if channel.id == 1129457187962499163:
        data = [
            {"role": "system", "content": "You are an AI assisstant that only responds in 2000 or less characters."},
            {"role": "user", "content": content[6:]}
        ]

        if len(content) > 2000:
            response = "Error: character limit (2000) exceeded."
        else:
            response = chat(data)
        await channel.send(response)

@bot.command()
async def ngpt(ctx):
    """Clear user chat memory"""
    channel = ctx.channel
    user_id = ctx.message.author.id
    if channel.id == 1129457187962499163:
        delete_memory(user_id)

# ----------------------------- FUNCTIONS ------------------------------ #

def run():
    """Start function"""
    bot.run(discord_token)
