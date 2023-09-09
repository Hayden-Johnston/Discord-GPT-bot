# author: Hayden Johnston
# date: 08/20/2023
# description: GPT-3 chatbot functions

import openai, os
from dotenv import load_dotenv
import db

if os.path.exists(".env") == True:
    load_dotenv()
openai.api_key = os.environ["OPENAITOKEN"]

# -------------------------------- GPT --------------------------------- #

def chat(data: list) -> str:
    """Chat with GPT-3 chatbot"""

    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = data
    )

    parsed_response = response['choices'][0]['message']['content']

    return parsed_response

# ---------------------------------------------------------------------- #

def handle_memory(id: int, prompt: str, response: str) -> None:
    """Handle user memory"""

    user_memory = db.get_by_id(id)

    if user_memory == []:
        # Create new user
        data = {"id": id, "memory": [prompt, response]}
        data["memory"] = ", ".join(data["memory"])
        db.insert_memory(data)

    else: 
        user_memory = user_memory[0][1].split(", ")
        user_memory.append(prompt)
        user_memory.append(response)
        if len(user_memory) > 4:
            user_memory.pop(0)
            user_memory.pop(0)
        user_memory = ", ".join(user_memory)
        db.update_memory({"id": id, "memory": user_memory})
