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

def handle_memory(id: int, prompt: str) -> None:
    """Handle user memory"""
    user_memory = db.get_by_id(id)

    if user_memory == None:
        # Create new user
        db.insert_memory({"id": id, "memory": [prompt]})

    else: 
        memory = user_memory
        memory.append(prompt)
        if len(memory) > 2:
            memory.pop(0)
        db.update_memory({"id": id, "memory": [memory]})
        prompt = memory