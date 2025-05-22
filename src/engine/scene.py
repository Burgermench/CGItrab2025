from OpenGL.GL import *
from charts.chart_loader import load_chart
from engine.lane import NoteLane
from engine.player import Player
from engine.audio import play_music
from engine.effects import EffectManager
import pygame



class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.effects = EffectManager()
        self.lanes = [NoteLane(i, key) for i, key in enumerate(self.player.keymap)]

    # notecharts + music
    self.chart = load_chart("charts/note_chart.json")
    self.song_start_time = pygame.time.get_ticks() / 1000
    self.song_started = True
    
    # spawn notes based on music time
    current_time = (pygame.time.get_ticks() - self.song_start_time) / 1000.0
    while self.chart_index < len(self.chart) and self.chart[self.chart_index]["time"] <= current_time:
        note_data
