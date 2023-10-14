import openai

KEY = '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'

openai.api_key = KEY


def generate_response(text):
    response = openai.Completion.create(
        prompt=text,  # текст который мы передаем GPT
        engine='text-davinci-003', # движок AI
        max_tokens=100, # макс. длина символов
        temperature=0.7, # уровень креативности AI
        n=1, # количество ответов
        stop=None, # стоп-слово
        timeout=15 # время на ответ
    )


    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None

res = generate_response('Привет как у тебя дела, какая погода сейчас в Минске?')
print(res)
