import openai
import os

openai.api_key = 'org-5RQHnnXwWpT9llTKlkSAY9pi'  # Replace with your actual API key

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    message = input("User: ")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        reply = chat.choices[0].message['content']
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
