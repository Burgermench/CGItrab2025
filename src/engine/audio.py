import pygame.mixer
from config import INSTRUMENT_SOUNDS

pygame.mixer.init()
sounds = {k: pygame.mixer.Sound(v) for k, v in INSTRUMENT_SOUNDS.items()}

def play_sound(name):
    if name in sounds:
        sounds[name].play()

def play_music(file_path):
    if file_path in sounds:
        pygame.mixer.music.load(sounds[file_path])
        pygame.mixer.music.play()