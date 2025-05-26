import pygame.mixer
import os
from config import INSTRUMENT_SOUNDS


pygame.mixer.init()


# load all instrument sfx files
sounds = {
    name: pygame.mixer.Sound(path)
    for name, path in INSTRUMENT_SOUNDS.items()
}

note_cache = {}
supported_formats = {".wav", ".mp3", ".ogg"}


def play_sound(name):
    if name in sounds:
        sounds[name].play()


def play_music(file_path):
    try:
        pygame.mixer.music.load(sounds[file_path])
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Failed to play music '{file_path}': {e}")
        
        
def play_note(note_name):
    if note_name in note_cache:
        note_cache[note_name].play()
        return
    base_path = "assets/sounds/notes"
    for ext in supported_formats:
        full_path = os.path.join(base_path, f"{note_name}{ext}")
        if os.path.exists(full_path):
            try:
                note_sound = pygame.mixer.Sound(full_path)
                note_cache[note_name] = note_sound
                note_sound.play()
                return
            except Exception as e:
                print(f"Failed to load {note_name}{ext}: {e}")
                return
    print(f"No sound found for note '{note_name}', (checked .wav/.mp3) formats")
    
def play_wrong_sound():
    try:
        sound = pygame.mixer.Sound("assets/sounds/wrong.mp3")
        sound.play()
    except:
        print(f"Couldn't play wrong key sound: {e}")
    