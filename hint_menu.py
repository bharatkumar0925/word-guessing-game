import pygame
from sound_music import audio_play
from user_input_checking import user_input

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


