# sound_music.py

import pygame
import threading

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

