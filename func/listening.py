import speech_recognition as sr

# Define the zikrs and the content of the sura
zikrs = ['alhamdulillah', 'subhanallah', 'allahu akbar']
sura_content = "Bismillahir-Rahmanir-Rahim. Alhamdu lillahi Rabbil 'alamin. Ar-Rahmanir-Rahim. Maliki yawmid-Din. Iyyaka na'budu wa iyyaka nasta'in. Ihdinas-siratal-mustaqim. Siratal-ladhina an'amta 'alayhim, ghayril-maghbubi 'alayhim wa lad-Dallin."

# Initialize counters
zikr_count = 0
sura_count = 0

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

# Main loop
while True:
    command = recognize_speech()
    
    if command == "stop":
        print("Program stopped.")
        break
    
    if command == "start":
        print("You said 'Start'.")
        
        while True:
            choice = recognize_speech()
            
            if choice == "zikrs":
                print("You chose 'zikrs'.")
                while True:
                    zikr = recognize_speech()
                    if zikr in zikrs:
                        zikr_count += 1
                        print(f"Zikr counted! Total Zikrs: {zikr_count}")
                    else:
                        print("Not a recognized zikr. Try again.")
            
            elif choice == "sura":
                print("You chose 'sura'. Please say the name of the sura.")
                sura_name = recognize_speech()
                print("Now say the content of the sura.")
                content = recognize_speech()
                if content == sura_content.lower():
                    sura_count += 1
                    print(f"Sura counted! Total Suras: {sura_count}")
                else:
                    print("The content does not match the sura.")
                    
            elif choice == "stop":
                print("Stopping the counting process.")
                break
            else:
                print("Invalid option. Please say 'zikrs' or 'sura'.")
