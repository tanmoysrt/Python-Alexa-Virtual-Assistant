import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

#############################################################
# Customise the name of your virtual assistant as your wish #
# The name must be in lower case                            #
#############################################################

virtual_assistant_name = 'alexa'

listener = sr.Recognizer()
engine = pyttsx3.init()
listener.dynamic_energy_threshold = False
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
website_list = {
    "facebook": "https://facebook.com/",
    "google": "https://google.com/",
    "instagram": "https://www.instagram.com/",
    "telegram": "https://web.telegram.org/",
    "spotify": "https://open.spotify.com/",
    "youtube": "https://youtube.com/",
    "whatsapp": "https://web.whatsapp.com/",
}


def talk(text, is_assistant=True):
    if is_assistant:
        print(f'{virtual_assistant_name.title()} : {text}')
        engine.say(text.lower())
        engine.runAndWait()
    else:
        print(f'User : {text}')


def recognise_command():
    command = None
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            print(listener.energy_threshold)
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            if virtual_assistant_name.lower() in command:
                command = str(command).replace(
                    str(virtual_assistant_name).lower(), '')
                talk(command, False)
    except:
        talk("Please tell again, I cannot hear you.")

    return command


def website_name_check_in_command(command):
    for i in str(command).split():
        for j in website_list.keys():
            if i == j:
                return website_list[j]
                break
    return None


talk("I am listening to you")
talk("What can i do for you")
while True:
    command = recognise_command()
    if command is not None:
        if 'play' in command:
            topic = command.replace('play', '')
            talk('Playing')
            pywhatkit.playonyt(topic)
        elif 'search' in command:
            command = command.replace('search', '')
            if 'in' in command:
                command = command.replace('in', '')
            if 'youtube' in command:
                commmand = command.replace('youtube', '')
                talk('Opening the video/music in youtube')
                pywhatkit.playonyt(command)
            elif 'wikipedia' in command:
                talk('Searching')
                command = command.replace('wikipedia', '')
                talk(wikipedia.summary(command, 1))
            else:
                if 'google' in command:
                    command = command.replace('google', '')
                talk('Opening browser and searching')
                pywhatkit.search(command)
        elif 'open' in command:
            command = command.replace('open', '')
            website = website_name_check_in_command(command)
            if website is not None:
                talk('Opening....')
                webbrowser.open(website, new=0)
            else:
                talk('I do not know this website')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            result = wikipedia.summary(person, 1)
            talk(result)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'your name' in command:
            talk(
                f"My name is {virtual_assistant_name.title()}. I am  your virtual assistant. Nice to meet you.")
        elif 'stop' in command:
            break
        else:
            talk("Sorry, I have no answer for your question.I am searching in google")
            pywhatkit.search(command)
