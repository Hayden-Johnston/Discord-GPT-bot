import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI-KEY"]

def chat(prompt: str) -> str:
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are an AI assisstant that only responds in 2000 or less characters."},
            {"role": "user", "content": prompt}
        ]
    )

    parsed_response = response['choices'][0]['message']['content']

    return parsed_response