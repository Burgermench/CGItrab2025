import pygame.mixer
import os
from config import INSTRUMENT_SOUNDS

pygame.mixer.init()

# load all instrument sfx files
sounds = {k: pygame.mixer.Sound(v) for k, v in INSTRUMENT_SOUNDS.items()}

note_cache = {}
supported_formats = {".wav", ".mp3"}

def play_sound(name):
    if name in sounds:
        sounds[name].play()

def play_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    except Exception as e:
        print(f"Error playing music: {e}")
        
def play_note(note_name):
    # play notes dynamically like "A1", "C2", etc, check virtual piano online on the browser to understand where the inspiration for this comes from
    # we look for files inside assets/sounds/notes
    if note_name in note_cache:
        note_cache[note_name].play()