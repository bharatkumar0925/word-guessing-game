import random
import docx
from tts_advance import text_to_speech
from sound_music import audio_play, background_music
from hint_menu import hint_menu
from user_input_checking import user_input
from game_score import get_high_score, set_high_score
import math

def words():
    try:
        doc = docx.Document('all words.docx')
    except:
        print('File not found. ')
    words = [para.text for para in doc.paragraphs]
    words_list = '\n'.join(words).split()
    random_word = random.choice(random.sample(words_list, 10))
    return random_word


def quit_game():
    print("Do you really want to quit? ")
    confirmation = input("Enter 1 for yes and anything  for no: ")
    if confirmation == '1':
        print('You quit the game. \n Thanks for playing... ')
        quit()
    else:
        pass


def score_condition(score, condition_triggered):
    for i, condition in enumerate([50, 100, 200]):
        if score >= condition and not condition_triggered[i]:
            messages = [
                "You completed his fifty! \n Keep it up!",
                "Hurray! You completed your century. Keep it up!",
                "You are continuously growing your score, and you are improving your game. You have set a record. Keep it up!!"
            ]
            audio_play('C:/Users/BHARAT/Desktop/my files/sounds/effects/positive1.mp3')
            text_to_speech(messages[i], duration=2)
            condition_triggered[i] = True




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
            'Press enter for play, \t 1 for hint,  \t 2 for change settings,  \t 3 for check highest score  \t 4 for quit the game \t  and otherwise write your answer. ')
        audio_play('C:/Users/BHARAT/Desktop/my files/sounds/effects/interface-124464.mp3')
        choice = user_input()

        if choice == '' or choice.isspace():
            text_to_speech(random_word, duration=0.75)
            continue

        if choice == '1':
            given_hint, score = hint_menu(given_hint, random_word, score)

        elif choice == '2':
            print(f'In this section you can change the voice, \n change the speed and pitch. ')
            text_to_speech(random_word, duration=1, change_voice=True, permanent_change=True)

        elif choice == '3':
            set_high_score(score, high_score)
            print('Your highest score is: ', high_score)

        elif choice == '4':
            quit_game()

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
