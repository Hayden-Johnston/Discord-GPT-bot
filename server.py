from quart import Quart, render_template, redirect, url_for, request, jsonify
from quart_discord import DiscordOAuth2Session
from dotenv import dotenv_values
import os
from gptfunctions import chat

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

config = dotenv_values(".env")

app = Quart(__name__)
app.secret_key = config["SECRET-KEY"]

app.config["DISCORD_CLIENT_ID"] = config["DISCORD-CLIENTID"]  # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = config["DISCORD-CLIENTSECRET"]  # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = config["DISCORD-REDIRECT-URI"]  # URL to your callback endpoint.

discord = DiscordOAuth2Session(app) #handle session for authentication

@app.route("/")
async def home():
    return await render_template("home.html", authorized=await discord.authorized)

@app.route("/login")
async def login():
    return await discord.create_session() # handles session creation for authentication

@app.route('/gpt', methods=['POST'])
async def gpt():
    data = await request.get_json()
    prompt = data["prompt"]
    response = chat(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)