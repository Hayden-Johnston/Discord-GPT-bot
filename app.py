# author: Hayden Johnston
# date: 08/20/2023
# description: GPT-3 chatbot functions

import openai, os
from dotenv import load_dotenv
from user_model import User
import db

if os.path.exists(".env") == True:
    load_dotenv()
openai.api_key = os.environ["OPENAI-TOKEN"]

# ---------------------------------------------------------------------- #

def chat(prompt: str, id: int) -> str:
    """Chat with GPT-3 chatbot"""
    
    # Check if user exists in database
    get_id = db.get_by_id(id)
    if get_id == None:
        # Create new user
        user = User(id)
        db.insert_memory({"user_id": user.id, "memory": prompt})

    else: 
        # Get user memory
        user = User(id)
        user.memory = get_id['memory']

    data_load = {"role": "user", "content": prompt}

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are an AI assisstant that only responds in 2000 or less characters."},
            data_load
        ]
    )

    parsed_response = response['choices'][0]['message']['content']

    return parsed_response