import speech_recognition as sr
import tkinter as tk
from threading import Thread

# Функция для распознавания речи
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            try:
                print("Слушаю...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='ru-RU')
                if "альхамдулилях" in text.lower():
                    update_count()
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("Ошибка сервиса распознавания.")
                break

# Функция для обновления счётчика
def update_count():
    global count
    count += 1
    count_label.config(text=f"Количество: {count}")

# Создание графического интерфейса
root = tk.Tk()
root.title("Счетчик Альхамдулилях")

count = 0
count_label = tk.Label(root, text=f"Количество: {count}", font=("Helvetica", 24))
count_label.pack(pady=20)

# Запуск потока для прослушивания микрофона
thread = Thread(target=listen, daemon=True)
thread.start()

# Запуск главного цикла интерфейса
root.mainloop()
