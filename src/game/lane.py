from game.note import Note
import pygame

class Lane:
    def __init__(self, index, key):
        self.index = index
        self.key = key
        self.notes = []

    def spawn_note(self, time):
        note = Note(self.index, time)
        self.notes.append(note)

    def update(self, dt):
        for note in self.notes:
            note.update(dt)

    def check_hit(self, pressed_keys):
        for note in self.notes:
            if pressed_keys[self.key] and note.is_hittable() and not note.hit:
                note.hit = True
                return True
        return False

    def remove_missed(self):
        self.notes = [n for n in self.notes if not n.is_missed()]