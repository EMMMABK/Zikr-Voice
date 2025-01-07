## Zikr Counter with Speech Recognition

This project implements a speech recognition-based zikr counter. It listens to voice commands and counts specific zikr repetitions in multiple languages (Russian and Arabic).

---

## Features
- Supports voice commands in Russian to **start** and **stop** the zikr counter.
- Recognizes and counts zikrs in both **Russian** and **Arabic**.
- Displays a summary of counted zikrs when stopped.

---

## Requirements

1. Python 3.x
2. Required Libraries:
   - `speechrecognition`
   - `pyaudio` or `portaudio`

To install the dependencies, run:
```
pip install SpeechRecognition pyaudio
```
> Note: On some systems, additional setup may be required for `pyaudio`.

---

## Usage

1. Prepare a list of zikrs in two languages (Russian and Arabic) and define them as:
   ```python
   ZIKR_LIST = ["Zikr1", "Zikr2"]
   ```
2. Replace `ZIKR_LIST` in the code with your predefined zikrs.

3. Run the script:
```
python zikr_counter.py
```

4. Speak the following commands in **Russian**:
   - **"ЗИКР СТАРТ"** - Starts the zikr counter and resets all counts.
   - **"ЗИКР СТОП"** - Stops the zikr counter and displays the results.

5. Begin reciting the zikrs. The counter will increment automatically when recognized.

---

## Example Output
```
Ожидание произношения зикра...
Говорите...
Счётчик запущен.
Zikr1: 1
Zikr2: 2
Счётчик остановлен.
Zikr1: 1
Zikr2: 2
```

---

## Error Handling
- If the audio is unclear or cannot be recognized, an error message will be displayed.
- Unrecognized zikrs will prompt a retry message.

---

## Notes
- The recognition accuracy depends on the quality of the microphone and ambient noise levels.
- The code uses **Google Speech Recognition**, which requires internet access.

---

## License
This project is licensed under the MIT License.

