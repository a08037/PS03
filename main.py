import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаем объект переводчика
translator = Translator()

# Функция для получения случайных английских слов с их определениями
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Получаем случайное слово и его определение
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его определение на русский
        translated_word = translator.translate(english_word, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        return {
            "english_word": english_word,
            "translated_word": translated_word,
            "word_definition": word_definition,
            "translated_definition": translated_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Функция для игры
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if word_dict:
            english_word = word_dict.get("english_word")
            translated_word = word_dict.get("translated_word")
            translated_definition = word_dict.get("translated_definition")

            print(f"Значение слова: {translated_definition}")
            user = input("Что это за слово? (Введите перевод на русском): ")

            if user.lower() == translated_word.lower():
                print("Все верно!")
            else:
                print(f"Ответ неверный! Было загадано слово: {translated_word} ({english_word})")

            play_again = input("Хотите сыграть еще раз? y/n: ")
            if play_again.lower() != "y":
                print("Спасибо за игру!")
                break

word_game()
