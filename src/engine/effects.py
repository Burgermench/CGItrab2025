
class EffectManager:
    def __init__(self):
        self.active_effect = None

    def update(self, dt, player):
        if player.combo >= 10:
            self.active_effect = "fire"
        elif player.combo >= 5:
            self.active_effect = "electricity"
        else:
            self.active_effect = None

    def render(self):
        # TODO: Render fire, electricity, etc. (OpenGL or particle system)
        if self.active_effect:
            print(f"Rendering {self.active_effect}")
