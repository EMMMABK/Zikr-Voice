import json
import speech_recognition as sr
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Specify the path to your JSON file
json_file_path = 'surahs.json'  # Adjust this path if necessary
print("Trying to open:", os.path.abspath(json_file_path))

# Check if the JSON file exists
if not os.path.isfile(json_file_path):
    print(f"Error: The file '{json_file_path}' does not exist.")
    exit()

# Load the JSON data from the file located in the 'json' folder
try:
    with open(json_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        print("File content before loading as JSON:")
        print(content)  # Print the content for debugging
        data = json.loads(content)  # Using json.loads instead of json.load
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
            return ""

def main():
    zikr_count = 0
    print("Say 'START' to begin.")
    command = listen_command()

    if command == 'start':
        print("Would you like to count a zikr or retrieve a surah? Say 'dhikr' or 'sura'.")
        command = listen_command()

        if command == 'dhikr':
            print("Please say a zikr from the list:")
            print(", ".join(data['zikrs']))
            zikr_to_count = listen_command()

            if zikr_to_count in data['zikrs']:
                print(f"Counting occurrences of '{zikr_to_count}'. Say 'STOP' to end.")
                while True:
                    command = listen_command()
                    if command == 'stop':
                        break
                    elif command == zikr_to_count:
                        zikr_count += 1
                        print(f"Count of '{zikr_to_count}': {zikr_count}")
            else:
                print("The zikr you mentioned is not in the list.")

        elif command == 'sura':
            print("Please say the name of the Surah.")
            surah_name = listen_command()

            if surah_name in data['surahs']:
                print(f"Content of Surah {surah_name}:")
                print(data['surahs'][surah_name]['content'])
            else:
                print("The Surah you mentioned is not in the list.")

if __name__ == "__main__":
    main()
