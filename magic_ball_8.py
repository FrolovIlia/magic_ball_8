import random
from time import sleep

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, МИР, я знаю ответ на любой твой вопрос.')
sleep(2)
print('Как я могу к Вам обращаться?')
name = input()
print('Привет', name, 'начнём пожалуй?', sep=', ')
sleep(2)

def main():
    print('Пожалуйста, введи беспокоящий тебя вопрос.')
    question = input()
    print(random.choice(answers))
    sleep(2)
    print('Хочешь задать ещё один вопрос? да/нет')

main()

while True:
    repeat = input()
    if repeat.lower() == 'да':
        main()
    if repeat.lower() == 'нет':
        print('Возвращайся если возникнут вопросы!')
        break

sleep(5)
