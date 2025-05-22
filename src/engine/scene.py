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
        self.chart = load_chart("charts/notechart.json")
        self.chart_index = 0
        self.song_started = False
        self.song_start_time = 0
        
    def update(self, dt):
        # start music when game starts
        if not self.song_started:
            play_music("assets/sounds/song.mp3")
            self.song_start_time = pygame.time.get_ticks()
            self.song_started = True
            
        # spawn notes based on music timing
        current_time = (pygame.time.get_ticks() - self.song_start_time) / 1000.0
        while self.chart_index < len(self.chart) and self.chart[self.chart_index]["time"] <= current_time:
            note_data = self.chart[self.chart_index]
            self.lanes[note_data["lane"]].spawn_note(note_data["instrument"])
            self.chart_index += 1
            
        for lane in self.lanes:
            lane.update(dt, self.player)
            
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        
        for lane in self.lanes:
            lane.render()
            
        # hit zone
        glColor3f(0.5, 1.0, 0.5)
        glBegin(GL_QUADS)
        glVertex3f(-1.2, -1.0, 0)
        glVertex3f(1.2, -1.0, 0)
        glVertex3f(1.2, -0.98, 0)
        glVertex3f(-1.2, -0.98, 0)
        glEnd()
        
        self.player.render()
        self.effects.render()
        

        
        
        
        
        
        
        
        