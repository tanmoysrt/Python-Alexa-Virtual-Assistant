import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#############################################################
# Customise the name of your virtual assistant as your wish #
# The name must be in lower case                            #
#############################################################

virtual_assistant_name = 'alexa'

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if virtual_assistant_name.lower() in command:
                command = str(command).replace(
                    str(virtual_assistant_name).lower(), '')
                talk(command, False)
    except:
        talk("Please tell again, I cannot hear you.")

    return command



talk("I am listening to you")
talk("What can i do for you")
while True:
    command = recognise_command()
    if command is not None:
        if 'play' in command:
            topic = command.replace('play', '')
            talk('Playing')
            pywhatkit.playonyt(topic)
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
            talk(f"My name is {virtual_assistant_name.title()}. I am  your virtual assistant. Nice to meet you.")
        elif 'stop' in command:
            break
        else:
            talk("Sorry, I have no answer for your question.")
