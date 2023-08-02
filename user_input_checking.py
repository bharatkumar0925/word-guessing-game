from sound_music import audio_play

# user_input_checking.py

def user_input(prompt='ANSWER:', digit=False, string=False):
    path = 'C:/Users/BHARAT/Desktop/my files/sounds/effects/'
    while True:

        ans = input(prompt)


        if digit and not ans.isdigit():
            audio_play(path+'windows-error-sound-effect-35894.mp3')
            print('Please type a digit!')
            continue

        elif string and not ans.isalpha():
            audio_play(path+'windows-error-sound-effect-35894.mp3')
            print('Please write a string!')
            continue

        elif not digit and not string:
            # If both digit and string are False, any input is allowed
            return ans


        else:
            # If either digit or string (or both) is True, only allow the respective input type
            return ans

