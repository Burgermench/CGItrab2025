from OpenGL.GL import *

LANE_WIDTH = 0.2
LANE_DEPTH = 2.0

class NoteLane:
    def __init__(self, index, key):
        self.index = index
        self.key = key
        self.notes = []
        
    def spawn_note(self, instrument):
        from .note import Note
        self.notes.append(Note(self.index, instrument))

    def update(self, dt, player):
        for note in self.notes:
            note.update(dt)
        #check for hits
        hit_notes = [n for n in self.notes if n.check_hit(player)]
        for n in hit_notes:
            self.notes.remove(n)
        #check for wrong key presses when NO notes are hitable
        if not hit_notes and player.is_key_down(self.index):
            from engine.audio import play_wrong_sound
            play_wrong_sound()
            player.on_miss()
            
    
    def render(self):
        x = (self.index - 4) * (LANE_WIDTH * 2)         # spread lanes from center

        # draw track
        glColor3f(0.2, 0.2, 0.2)
        glBegin(GL_QUADS)
        glVertex3f(x - LANE_WIDTH, -1.0, 0)
        glVertex3f(x + LANE_WIDTH, -1.0, 0)
        glVertex3f(x + LANE_WIDTH, -1.0, -LANE_DEPTH)
        glVertex3f(x - LANE_WIDTH, -1.0, -LANE_DEPTH)
        glEnd()

        # draw notes
        for note in self.notes:
            note.render(x)