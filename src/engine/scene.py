from OpenGL.GL import *

def render(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)

    for lane in self.lanes:
        lane.render()

    # Draw hit zone bar
    glColor3f(0.5, 1.0, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-1.2, -1.0, 0)
    glVertex3f(1.2, -1.0, 0)
    glVertex3f(1.2, -0.98, 0)
    glVertex3f(-1.2, -0.98, 0)
    glEnd()

    self.player.render()
    self.effects.render()