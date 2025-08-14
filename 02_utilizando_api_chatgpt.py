import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

MODELO = "gpt-3.5-turbo"

def retorna_resposta_modelo(mensagens, openai_key, modelo=MODELO, temperatura=0, stream=False):
  openai.api_key = openai_key
  response = openai.ChatCompletion.create(
    model=modelo,
    messages=mensagens,
    temperature=temperatura,
    stream=stream
  )
  
  return response.choices[0].message.content

mensagens = [{ "role": "user", "content": "O que é uma maça em cinco palavras?"}]
resposta = retorna_resposta_modelo(mensagens, openai_key)
print(resposta)