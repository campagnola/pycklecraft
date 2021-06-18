import math


class Player:
    def __init__(self, data):
        self.data = data
        for k, v in data.items():
            setattr(self, k, v)

    @property
    def x(self):
        return math.floor(self.position[0])

    @property
    def y(self):
        return math.floor(self.position[1])

    @property
    def z(self):
        return math.floor(self.position[2])
