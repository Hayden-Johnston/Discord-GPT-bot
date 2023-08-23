# author: Hayden Johnston
# date: 08/20/2023
# description: GPT-3 chatbot functions

import openai, os
from dotenv import load_dotenv
import db

if os.path.exists(".env") == True:
    load_dotenv()
openai.api_key = os.environ["OPENAI-TOKEN"]

# ---------------------------------------------------------------------- #

data_load = {"role": "user", "content": prompt}

def chat(prompt: str) -> str:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are an AI assisstant that only responds in 2000 or less characters."},
            data_load
        ]
    )

    parsed_response = response['choices'][0]['message']['content']

    return parsed_response

def check_memory(user_id):
    """Check user chat memory"""
    memory = db.get_by_id(user_id)['memory']
    return memory

def create_memory(user_id, content):
    """Create user chat memory"""
    data = {"user_id": user_id, "memory": [content]}
    db.insert_memory(data)
    
def update_memory(user_id, content, memory):
    """Update user chat memory"""
    data = {"user_id": user_id, "memory": content}
    db.update_memory(data)

def delete_memory(user_id):
    """Delete user chat memory"""
    db.delete_memory(user_id)