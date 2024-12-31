import speech_recognition as sr

# Хранилище для зикров
zikr_list = ["Аллаху Акбар", "Субханаллах", "Альхамдулиллах"]

# Переменные для состояния и счётчика
zikr_counter = 0
is_running = False

def recognize_zikr():
    global zikr_counter, is_running
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Ожидание произношения зикра...")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            while True:
                print("Говорите...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='ru').upper()

                if text == "ЗИКР СТАРТ":
                    zikr_counter = 0
                    is_running = True
                    print("Счётчик запущен.")
                elif text == "ЗИКР СТОП":
                    is_running = False
                    print(f"Счётчик остановлен. Итоговое количество: {zikr_counter}")
                elif is_running and text in zikr_list:
                    zikr_counter += 1
                    print(f"Зикр: {text}. Счётчик: {zikr_counter}")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

# Основной цикл для обработки команд
recognize_zikr()
