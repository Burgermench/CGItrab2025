from OpenGL.GL import *

class EffectManager:
    def __init__(self):
        self.active_effect = None
        self.intensity = 0.0


    def update(self, dt, player):
        if player.combo >= 10:
            self.active_effect = "fire"
        elif player.combo >= 5:
            self.active_effect = "electricity"
        elif player.combo >= 2:
            self.active_effect = "smoke"
        else:
            self.active_effect = None

        self.intensity = dt * 2 if self.active_effect else -dt * 2
        self.intensity = max(0.0, min(1.0, self.intensity))


    def render(self):
        if not self.active_effect or self.intensity <= 0:
            return
        
        glPushMatrix()
        glLoadIdentity()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        if self.active_effect == "fire":
            glColor4f(1.0, 0.3, 0.0, 0.25 * self.intensity)
        elif self.active_effect == "electricity":
            glColor4f(0.3, 0.6, 1.0, 0.25 * self.intensity)
        elif self.active_effect == "smoke":
            glColor4f(0.5, 0.5, 0.5, 0.15 * self.intensity)

        glBegin(GL_QUADS)
        glVertex2f(-1, -1)
        glVertex2f(1, -1)
        glVertex2f(1, 1)
        glVertex2f(-1, 1)
        glEnd()

        glDisable(GL_BLEND)
        glPopMatrix()
