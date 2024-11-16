import os
from mistralai import Mistral
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем API-ключ из .env
api_key = os.getenv('MISTRAL_API_KEY')
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def send_message(user_input):
    stream_response = client.chat.stream(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_input,
            },
        ]
    )

    response_content = ""
    for chunk in stream_response:
        response_content += chunk.data.choices[0].delta.content
        print(chunk.data.choices[0].delta.content, end='', flush=True)

    print()
    return response_content

def main():
    print("Welcome to the Mistral AI Chat App!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        print("Mistral AI:", end=' ')
        send_message(user_input)

if __name__ == "__main__":
    main()
