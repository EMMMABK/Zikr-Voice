import speech_recognition as sr
import tkinter as tk
from threading import Thread

# Функция для загрузки слов из файла
def load_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file.readlines()]

# Загрузка мусульманских слов из файла
all_words = load_words('words.txt')
count = 0

# Функция для распознавания речи
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                print("Слушаю...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='ru-RU')
                check_words(text.lower())
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("Ошибка сервиса распознавания.")
                break

# Функция для проверки слов и обновления счётчика
def check_words(text):
    global count
    for word in all_words:
        if word in text:
            count += 1
            update_count()
            break  # Убедитесь, что каждое слово считается только один раз за одно произнесение

# Функция для обновления счётчика
def update_count():
    count_label.config(text=f"Количество: {count}")

# Создание графического интерфейса
root = tk.Tk()
root.title("Счетчик Мусульманских Слов")

count_label = tk.Label(root, text=f"Количество: {count}", font=("Helvetica", 24))
count_label.pack(pady=20)

# Запуск потока для прослушивания микрофона
thread = Thread(target=listen, daemon=True)
thread.start()

# Запуск главного цикла интерфейса
root.mainloop()
