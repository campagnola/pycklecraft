from .player import Player


class Event:
    def __init__(self, data):
        self.data = data
        self.event = data['event']
        self.command = data['command']

    @property
    def player(self):
        return Player(self.data['player'])
