from .player import Player


class Event:
    def __init__(self, data):
        self.data = data
        self.type = data['type']

    @property
    def player(self):
        return Player(self.data['player'])

    @property
    def command(self):
        return self.data['command']
