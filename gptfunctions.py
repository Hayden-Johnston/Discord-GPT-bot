import openai, os
from dotenv import load_dotenv

if os.path.exists(".env") == True:
    load_dotenv()
openai.api_key = os.environ["OPENAI-TOKEN"]

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