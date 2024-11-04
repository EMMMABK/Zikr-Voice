import sounddevice as sd
import numpy as np
import speech_recognition as sr
import tkinter as tk
from threading import Thread

# Функция для загрузки слов из файла
def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []

# Загрузка мусульманских слов из файла
all_words = load_words('words.txt')
count = 0

# Функция для распознавания речи
def listen():
    recognizer = sr.Recognizer()
    samplerate = 44100  # Частота дискретизации

    while True:
        try:
            print("Слушаю...")
            # Запись аудио с помощью sounddevice
            audio_data = sd.rec(int(samplerate), samplerate=samplerate, channels=1, dtype='int16')
            sd.wait()  # Ожидание завершения записи

            # Преобразование в AudioData для распознавания
            audio_data = sr.AudioData(audio_data.tobytes(), samplerate, 2)  
            text = recognizer.recognize_google(audio_data, language='ru-RU')
            check_words(text.lower())
        except sr.UnknownValueError:
            continue
        except sr.RequestError:
            print("Ошибка сервиса распознавания.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Функция для проверки слов и обновления счётчика
def check_words(text):
    global count
    found_words = [word for word in all_words if word in text]
    if found_words:
        count += len(found_words)  # Увеличиваем счётчик на количество найденных слов
        update_count()

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
