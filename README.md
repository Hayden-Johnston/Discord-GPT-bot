# Discord-GPT-bot
Self-hosted Discord bot to query gpt-3. <br>
Maintains discrete chat memory for each user with SQLite to allow continued conversation. <br>
By default the database will maintain the last 2 messages from the user and system with a **400 Character limit** for any query or response.
*Due to the 2000 character limit of the gpt api and the possibility of handling up to 5 messages in a query, 400 characters is a safe starting point*

## Setup
Provide API keys through .env or docker configuration. <br>
Run main.py or build docker container and deploy.

## Commands
**/gpt** - Send query to Chat-GPT and the bot will output a response.  <br>
Bot will save the last 2 messages from both the user and bot and send with the next query to maintain chat memory.
<br>
**/gpt-n** - User resets their chat memory to begin a new conversation.
<br>
**/gpt-d** - Allow the system to deliver a more detailed response by removing the character limit imposed by chat memory - **Does not utilize chat memory** <br>
<br>
<br>
<br>
![Hx_a_curator_robot_for_the_code_nexus_named_qr8r_phonetic_curat_67dd02e2-657c-4113-844a-d55346651009](https://github.com/Hayden-Johnston/Discord-GPT-bot/assets/103093070/3b1e1aec-d582-4757-9e72-edda21cba46e)
