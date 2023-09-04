# Discord-GPT-bot
Self-hosted Discord bot to query gpt-3. <br>

## Database
Maintains discrete chat memory for each user with SQLite to allow continued conversation. <br>
By default the database will maintain the last 2 messages from the user and system with a **400 Character limit** for any query or response.
The command /gpt-d allows a user to raise the character limit to 2000 without utilizing chat memory, this is the limit of the gpt api.

## Commands
**/gpt** - Send query to Chat-GPT and the bot will output a response.  Utilizes chat memory.  <br>
<br>
**/gpt-d** - Allow the system to deliver a more detailed response by removing the character limit imposed by chat memory - **Does not utilize chat memory** 
<br>
**/gpt-n** - User resets their chat memory to begin a new conversation.
<br>

## Setup
Provide API keys through .env or docker configuration. <br>
Run main.py or build docker container and deploy.

<br>
<br>
<br>

![Hx_a_curator_robot_for_the_code_nexus_named_qr8r_phonetic_curat_67dd02e2-657c-4113-844a-d55346651009](https://github.com/Hayden-Johnston/Discord-GPT-bot/assets/103093070/3b1e1aec-d582-4757-9e72-edda21cba46e)
