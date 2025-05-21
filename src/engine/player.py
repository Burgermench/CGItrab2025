import pygame
from config import LANE_KEYS, COMBO_MAX

class Player:
    def __init__(self):
        self.keymap = LANE_KEYS
        self.combo = 0
        self.score = 0
        self.combo_ready = False

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.combo_ready = self.combo >= COMBO_MAX and keys[pygame.K_SPACE]

    def is_key_down(self, index):
        key = self.keymap[index]
        return pygame.key.get_pressed()[getattr(pygame, f"K_{key}")]

    def on_note_hit(self, instrument):
        self.score += 100 * (1 + self.combo // 10)
        self.combo += 1
        print(f"Hit! Instrument: {instrument}, Combo: {self.combo}, Score: {self.score}")

    def render(self):
        # Placeholder: Combo bar HUD
        pass
