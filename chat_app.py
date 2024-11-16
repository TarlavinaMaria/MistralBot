import os
from mistralai import Mistral # Импортируем Mistral AI
from dotenv import load_dotenv 

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем API-ключ из .env
api_key = os.getenv('MISTRAL_API_KEY')
model = "mistral-large-latest" 

client = Mistral(api_key=api_key) # Создаем экземпляр Mistral AI с API-ключом

def send_message(user_input):
    """Отправляет сообщение в Mistral AI и возвращает ответ."""
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
        # Цикл, который проходит по всем частям потокового ответа
        # Выводит текущую часть ответа на экран в реальном времени
        # Параметр end='' указывает, что не нужно добавлять новую строку после каждой части ответа, а flush=True гарантирует, что вывод будет немедленным
        response_content += chunk.data.choices[0].delta.content 
        print(chunk.data.choices[0].delta.content, end='', flush=True) 

    print() # Добавляем новую строку после вывода ответа
    return response_content

def main():
    print("Welcome to the Mistral AI Chat App!")
    print("Type 'exit' to end the conversation.")

    while True:
        # Бесконечный цикл, который запускает чат, пока пользователь не введет 'exit'
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        print("Mistral AI:", end=' ')
        send_message(user_input)

if __name__ == "__main__":
    main()
