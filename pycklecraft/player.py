import math


class Player:
    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data['name']

    @property
    def rotation(self):
        return self.data['rotation']

    @property
    def position(self):
        return self.data['position']

    @property
    def x(self):
        return math.floor(self.position[0])

    @property
    def y(self):
        return math.floor(self.position[1])

    @property
    def z(self):
        return math.floor(self.position[2])


