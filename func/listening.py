import speech_recognition as sr

# Хранилище для зикров
zikr_list = ZIKR_LIST
arabic_zikr_list = ZIKR_LIST_ARAB

# Переменные для состояния и счётчика
zikr_counter = {}
is_running = False

# Инициализация счётчика для каждого зикра
for zikr in zikr_list:
    zikr_counter[zikr] = 0

# Функция для распознавания речи и подсчёта зикров
def recognize_zikr():
    global is_running
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Ожидание произношения зикра...")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            while True:
                print("Говорите...")
                audio = recognizer.listen(source)

                try:
                    # Распознавание текста на русском для команд
                    text = recognizer.recognize_google(audio, language='ru').upper()
                except Exception as e:
                    print(f"Ошибка распознавания: {str(e)}")
                    continue

                if text == "ЗИКР СТАРТ":
                    for zikr in zikr_list:
                        zikr_counter[zikr] = 0
                    is_running = True
                    print("Счётчик запущен.")
                elif text == "ЗИКР СТОП":
                    is_running = False
                    print("Счётчик остановлен.")
                    for zikr, count in zikr_counter.items():
                        print(f"{zikr}: {count}")
                elif is_running:
                    # Распознавание зикров на двух языках
                    try:
                        zikr_text = recognizer.recognize_google(audio, language='ru').upper()
                    except:
                        zikr_text = recognizer.recognize_google(audio, language='ar')

                    if zikr_text in zikr_list:
                        zikr_counter[zikr_text] += 1
                        print(f"{zikr_text}: {zikr_counter[zikr_text]}")
                    elif zikr_text in arabic_zikr_list:
                        matched_zikr = zikr_list[arabic_zikr_list.index(zikr_text)]
                        zikr_counter[matched_zikr] += 1
                        print(f"{matched_zikr}: {zikr_counter[matched_zikr]}")
                    else:
                        print(f"Неизвестный зикр: {zikr_text}. Попробуйте снова.")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

# Основной цикл для обработки команд
recognize_zikr()
