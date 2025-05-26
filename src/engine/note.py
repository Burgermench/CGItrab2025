from OpenGL.GL import *
from config import NOTE_SPEED, NOTE_HIT_TOLERANCE

NOTE_RADIUS = 0.1

class Note:
    def __init__(self, lane_index, instrument):
        self.y = 1.5
        self.instrument = instrument
        self.hit = False


    def update(self, dt):
        self.y -= NOTE_SPEED * dt


    def check_hit(self, player):
        if self.hit:
            return False
        if abs(self.y) < NOTE_HIT_TOLERANCE and player.is_key_down(self.instrument):
            player.on_note_hit(self.instrument)
            self.hit = True
            return True
        return False


    def render(self, x):
        if self.hit: return

        glColor3f(1.0, 0.8, 0.1)
        glBegin(GL_QUADS)
        glVertex3f(x - NOTE_RADIUS, -1.0, -self.y)
        glVertex3f(x + NOTE_RADIUS, -1.0, -self.y)
        glVertex3f(x + NOTE_RADIUS, -1.0 + NOTE_RADIUS * 2, -self.y)
        glVertex3f(x - NOTE_RADIUS, -1.0 + NOTE_RADIUS * 2, -self.y)
        glEnd()