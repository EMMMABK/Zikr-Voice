import speech_recognition as sr

def count_zikr(text, zikr_words):
    count = 0
    for word in zikr_words:
        count += text.lower().count(word.lower())
    return count

# Задать список зикров
zikr_words = ["субхан Аллах", "альхамдулиллах", "Аллаху Акбар", "ла илаха илля Аллах"]

# Инициализировать распознаватель речи
recognizer = sr.Recognizer()

def start_recording():
    with sr.Microphone() as source:
        print("Пожалуйста, говорите...")
        audio = recognizer.listen(source)
        print("Запись завершена.")

    # Попробовать распознать речь
    try:
        text = recognizer.recognize_google(audio, language='ru-RU')
        print(f"Распознанный текст: {text}")

        # Сохранить текст в файл
        with open('words.txt', 'a', encoding='utf-8') as file:
            file.write(text + '\n')

        # Подсчитать и вывести количество зикров
        total_zikr = count_zikr(text, zikr_words)
        print(f"Количество зикров: {total_zikr}")

    except sr.UnknownValueError:
        print("Не удалось распознать речь.")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания: {e}")

def listen_for_commands():
    with sr.Microphone() as source:
        print("Пожалуйста, говорите команду (старт/стоп)...")
        audio = recognizer.listen(source)

    # Попробовать распознать речь
    try:
        command = recognizer.recognize_google(audio, language='ru-RU').strip().lower()
        print(f"Распознанная команда: {command}")
        return command
    except sr.UnknownValueError:
        print("Не удалось распознать команду.")
        return None
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания: {e}")
        return None

def main():
    while True:
        command = listen_for_commands()
        if command == "старт":
            start_recording()
        elif command == "стоп":
            print("Остановка записи.")
            break
        else:
            print("Неизвестная команда. Пожалуйста, используйте 'старт' или 'стоп'.")

if __name__ == "__main__":
    main()
