from dotenv import dotenv_values
import discord

config = dotenv_values(".env")

client = discord.Client(intents=discord.Intents.default())

@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(config["DISCORD-TOKEN"])