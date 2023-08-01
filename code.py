import math
import random
import docx
import pyttsx3
import time
import pygame
import threading

def user_input(prompt='ANSWER:', digit=False, string=False):
    while True:
        ans = input(prompt)

        if digit and not ans.isdigit():
            print('Please type a digit!')
            continue

        if string and not ans.isalpha():
            print('Please write a string!')
            continue

        if not digit and not string:
            # If both digit and string are False, any input is allowed
            return ans

        if ans.strip() == '':
            audio_play("C:/Users/BHARAT/Desktop/my files/sounds/effects/invalidSelection.mp3")
            print('No input detected!')
        else:
            # If either digit or string (or both) is True, only allow the respective input type
            return ans

def words():
    try:
        doc = docx.Document('all words.docx')
    except:
        print('File not found. ')

    words = [para.text for para in doc.paragraphs]
    words_list = '\n'.join(words).split()
    random_word = random.choice(random.sample(words_list, 10))
    return random_word


def text_to_speech(text, duration=2, voice=-1, speed=125, pitch=50, change_voice=False):

    # Select and set the voice, speed, pitch and volume
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)

        # If change_voice is True, prompt the user to select a voice
    if change_voice:
        print("Select a voice:")
        for i, v in enumerate(voices):
            print(f"{i}: {v.name}")
        voice_input = user_input(prompt="Enter the voice number:", digit=True)
        voice_input = int(voice_input)
        if 0 <= voice_input < len(voices):
            voice = voice_input
        else:
            print("Invalid voice selection. Using default voice.")

    engine.setProperty('rate', speed)  # You can adjust the value as needed, default is 150


    engine.setProperty('pitch', pitch)  # You can adjust the value as needed, default is 50
    engine.setProperty('volume', 1.0)  # You can adjust the value as needed, default is 2.0

        # Convert text to speech
    time.sleep(duration)
    engine.say(text)
        # Run the engine and wait until speech is finished
    engine.runAndWait()

def audio_play(sound_path='C:/Users/BHARAT/Desktop/my files/sounds/effects/correct.mp3', volume=100):
    #inside one more function for play sound so we can apply threading:
    def audio_play_inside(sound_path):
        pygame.init()
        pygame.mixer.init()
        try:
            sound = pygame.mixer.Sound(sound_path)
            sound.play()
            sound.set_volume((volume//100))
            pygame.time.wait(int(sound.get_length() * 1000))
        except pygame.error as e:
            print("Pygame related error, error occur during playing the sound.", str(e))
            pygame.mixer.stop()
            pygame.quit()

    thread = threading.Thread(target=audio_play_inside, args=(sound_path,))
    thread.start()


def background_music(sound_path='C:/Users/BHARAT/Desktop/my files/sounds/musics/8-bit-arcade-138828.mp3', volume=10):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.set_volume((volume / 100))
    pygame.mixer.music.play(-1)



"""Here is the function who colours the screen according the values so we can call according to our need and colour the screen in any color
using RGB value, which are between 0 to 255"""
def colour_screen(screen = (640, 480), colour=(255, 255, 255)):
    screen.fill(colour)
    pygame.init()
    screen = pygame.display.set_mode(screen)
    pygame.display.update()


def quit_game():
    print("Do you really want to quit? ")
    confirmation = input("Enter 1 for yes and anything  for no: ")
    if confirmation == '1':
        print('You quit the game. \n Thanks for playing... ')
        quit()
    else:
        pass


def hint_menu(given_hint, random_word, score):
    def play_sound_hint(sound_path):
        try:
#            pygame.init()
#            pygame.mixer.init()
            channel = pygame.mixer.Channel(0)
            sound = pygame.mixer.Sound(sound_path)
            channel.set_volume(0.35)
            channel.play(sound, loops=-1)
        except:
            pass


    if given_hint:
        print("You've already been given a hint for this word. Try guessing the word!")
        return given_hint, score
    print(
        f"Hint manue \n if you want to know first character of the word, enter 1: \n if you want to know length of the word enter 2: \n if you want to know first character of the word and length of the word, enter 3: \n If you want to know any character of the word then press 4 :\n otherwise press any key to exit the hint manue. \n ")
    first_char_word = "The first character of the word is: "
    length_word = "The length of the word is: "
    play_sound_hint('C:/Users/BHARAT/Desktop/my files/sounds/effects/gameImergency.wav')
    hint_input = user_input(prompt='What do you want to do:')


    if hint_input == '1':
        print(first_char_word, random_word[0])
    elif hint_input == '2':
        print(length_word, len(random_word))
    elif hint_input == '3':
        print(first_char_word, random_word[0], " and ", length_word, len(random_word))
        score -= 1
        audio_play("C:/Users/BHARAT/Desktop/my files/sounds/effects/dingIdea.mp3")
    elif hint_input == '4':
        any_length_char_input = user_input(prompt='Which number character you want to know:', digit=True)
        any_length_char_input = int(any_length_char_input)
        if any_length_char_input <= len(random_word):
            suffix = 'th'
            if any_length_char_input%10 == 1:
                suffix = 'st'
            elif any_length_char_input%10 == 2:
                suffix = 'nd'
            elif any_length_char_input%10 == 3:
                suffix = 'rd'
            print(f"The {any_length_char_input}{suffix} character of the word is: {random_word[any_length_char_input-1]}")
            score = score-1
            audio_play("C:/Users/BHARAT/Desktop/my files/sounds/effects/dingIdea.mp3")


        else:
            print("Word length is lower than your input. please enter correct input. ")
            given_hint = False
            return given_hint, score


    else:
        given_hint = False
        return given_hint, score

    given_hint = True
    pygame.mixer.stop()
    return given_hint, score



def score_condition(score, condition_triggered):
    for i, condition in enumerate([50, 100, 200]):
        if score >= condition and not condition_triggered[i]:
            messages = [
                "You completed his fifty! \n Keep it up!",
                "Hurray! You completed your century. Keep it up!",
                "You are continuously growing your score, and you are improving your game. You have set a record. Keep it up!!"
            ]
            audio_play('C:/Users/BHARAT/Desktop/my files/sounds/effects/positive1.mp3')
            text_to_speech(messages[i], voice=1, duration=2)
            condition_triggered[i] = True


def get_high_score():
    file_path = 'high_score.txt'
    try:
        with open(file_path, 'r') as file:
            return int(file.read())
    except:
        with open(file_path, 'w') as file:
            file.write('0')
            return 0


def set_high_score(score, high_score):
    if score > high_score:
        with open('high_score.txt', 'w') as file:
            file.write(str(score))





def game():
    audio_play("C:/Users/BHARAT/Desktop/my files/sounds/effects/winterHoliday.mp3", volume=100)
    background_music()
    score = 0
    correct_word = 0
    high_score = get_high_score()
    given_hint = False  # Track the hint whethre given or not?
    condition_triggered = [False, False, False]

    random_word = words()
    text_to_speech(random_word)

    while True:
        print(
            'Enter 1 for play, \t 2 for quit  \t 3 for hint,  \t 4 for check highest score \t and otherwise write your answer. ')
        audio_play('C:/Users/BHARAT/Desktop/my files/sounds/effects/interface-124464.mp3')
        choice = user_input()
#        if choice == "":
#            print('No input detected. Try again. ')
#            continue



        if choice == '1':
            text_to_speech(random_word, duration=0.75)

        elif choice == '2':
            quit_game()
        elif choice == '3':
            given_hint, score = hint_menu(given_hint, random_word, score)

        elif choice == '4':
            set_high_score(score, high_score)
            print('Your highest score is: ', high_score)
        elif choice == '5':
            print(f'In this section you can change the voice, \n change the speed and pitch. ')
            voice_input = user_input(prompt='select 0, 1 and 2')
            voice_input = int(voice_input)
            text_to_speech(random_word, voice=voice_input, duration=1, change_voice=True)

        else:
            if choice.strip().lower() == random_word.strip().lower():
                audio_play()
                score = score + (math.ceil(len(random_word) / 2))
                correct_word += 1
                print(f'Your answer is right! \n Your score is:  {score}')
                score_condition(score, condition_triggered)

                random_word = words()
                text_to_speech(random_word, duration=0.75)
                given_hint = False  # Reset hint  for new word
                continue


            else:
                audio_play("C:/Users/BHARAT/Desktop/my files/sounds/effects/wrong1.mp3")
                print(f'Your answer is wrong! \n your final score is:  {score}')
                print(f"You total give {correct_word} correct answer. ")
                print('The write answer is:  \n', random_word)
                spell_word = ''.join([c + ', ' for c in random_word])
                text_to_speech(f'The write answer is: {random_word} \n spelling of {random_word} is: {spell_word}', duration=1, speed=180)
                pygame.mixer.music.stop()
                pygame.quit()
                if score > high_score:
                    set_high_score(score, high_score)
                    audio_play('C:/Users/BHARAT/Desktop/my files/sounds/musics/longclap-33152.mp3')
                    text_to_speech(
                        f'Congratulation! You set a new high score. \n your new high score is: {score} \n and your previous high score was: {high_score}',
                    duration=15)

            break

def game_play():
    game()
    while True:
        game_input = input("Enter 1 for play or any number for quit: ")
        if game_input == '1':
            game()
            continue
        else:
            print('Good bye. ')
        break

game_play()
