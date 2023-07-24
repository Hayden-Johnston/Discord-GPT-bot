from quart import Quart, render_template, redirect, url_for, request, jsonify
from quart_discord import DiscordOAuth2Session
import os
from gptfunctions import chat

os.environ[
    "OAUTHLIB_INSECURE_TRANSPORT"
] = "1"

app = Quart(__name__)


app.config["SECRET_KEY"] = "test123"

app.config["DISCORD_CLIENT_ID"] = 969522874446671953  # Discord client ID.
app.config[
    "DISCORD_CLIENT_SECRET"
] = "dfp9GSgUHqvIMBSEIsrG9DW1XMnJskhl"  # Discord client secret.
app.config[
    "DISCORD_REDIRECT_URI"
] = "http://127.0.0.1:5000/callback"  # URL to your callback endpoint.

discord = DiscordOAuth2Session(app) #handle session for authentication

@app.route('/gpt', methods=['POST'])
async def gpt():
    data = await request.get_json()
    prompt = data["prompt"]
    response = chat(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)