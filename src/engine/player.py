import pygame
from engine.audio import play_note, play_sound
from config import COMBO_MAX, LANE_KEYS, LANE_NOTES
from engine.audio import play_sound


class Player:
    def __init__(self):
        self.keymap = LANE_KEYS
        self.combo = 0
        self.score = 0
        self.combo_ready = False


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.combo_ready = self.combo >= COMBO_MAX and keys[pygame.K_SPACE]
        if self.slowmo > 0:
            dt *= 0.5    # Apply slow motion effect


    def is_key_down(self, index):
        key = self.keymap[index]
        pressed = pygame.key.get_pressed()[
            getattr(pygame, f"K_{key}")
        ]
        if pressed:
            self.last_hit_index = index
        return pressed


    def on_note_hit(self, instrument):
        self.score += 100 * (1 + self.combo // 10)
        self.combo += 1
        print(f"Hit! Instrument: {instrument}, Combo: {self.combo}, Score: {self.score}")
        play_sound(instrument)

        
    def on_miss(self):
        print("Miss!")
        self.combo = 0
        self.combo_ready = False
        self.slowmo = 30         #frames of slow motion effect


    def render(self):
        # Placeholder: Combo bar HUD
        pass
