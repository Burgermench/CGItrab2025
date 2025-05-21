class Note:
    def __init__(self, lane_index, spawn_time, speed=2.0):
        self.lane_index = lane_index
        self.spawn_time = spawn_time
        self.speed = speed
        self.z = 10.0               # starting Z position
        self.hit = False

    def update(self, dt):
        self.z -= self.speed * dt

    def is_hittable(self):
        return 0.8 <= self.z <= 1.2

    def is_missed(self):
        return self.z < 0.5 and not self.hit