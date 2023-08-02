# tts_advance.py
import pyttsx3
import time
import configparser
from user_input_checking import user_input

# Define a global variable to store the default voice
default_voice = -1
default_speed = 125
default_pitch = 50

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Voice' in config:
        global default_voice, default_speed, default_pitch
        default_voice = int(config['Voice']['default_voice'])
        default_speed = int(config['Voice']['default_speed'])
        default_pitch = int(config['Voice']['default_pitch'])

def save_config():
    config = configparser.ConfigParser()
    config['Voice'] = {'default_voice': str(default_voice),
                       'default_speed': str(default_speed),
                       'default_pitch': str(default_pitch)}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def text_to_speech(text, duration=2, speed=default_speed, pitch=default_pitch,
                   change_voice=False, permanent_change=False):
    global default_voice  # Access the global variable

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if change_voice:
        print("Select a voice:")
        for i, v in enumerate(voices):
            print(f"{i}: {v.name}")
        voice_input = user_input(prompt="Enter the voice number:", digit=True)
        voice_input = int(voice_input)
        if 0 <= voice_input < len(voices):
            default_voice = voice_input  # Store the selected voice
            save_config()  # Save the selected voice to the configuration file
            if permanent_change:
                engine = pyttsx3.init()  # Reinitialize engine for permanent change
        else:
            print("Invalid voice selection. Using default voice.")

    load_config()  # Load configuration before setting voice
    engine.setProperty('voice', voices[default_voice].id)
    engine.setProperty('rate', speed)
    engine.setProperty('pitch', pitch)
    engine.setProperty('volume', 1.0)

    # Convert text to speech
    time.sleep(duration)
    engine.say(text)
    engine.runAndWait()

# Load initial configuration
load_config()
