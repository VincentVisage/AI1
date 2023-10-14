import openai

KEY = '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'

openai.api_key = KEY


def generate_response(text):
    response = openai.Completion.create(
        prompt=text,  # текст который мы передаем GPT
        engine='text-davinci-003', # движок AI
        max_tokens=100, # макс. длина символов
        tempature=0.7, # уровень креативности AI
        n=1, # количество ответов
        stop=None, # стоп-слово
        timeout=15 # время на ответ

    )