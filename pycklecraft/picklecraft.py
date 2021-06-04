import json
import socket
import requests
import threading


class PicklecraftClient:
    def __init__(self, server='localhost', port=3200, verbose=False):
        self.verbose = verbose
        self.server = server
        self.port = port
        self._on_command = None
        self.listen_thread = threading.Thread(target=self._listen, daemon=True)
        self.listen_thread.start()


    @property
    def players(self):
        return self._get('/players')

    def set_on_command(self, callback):
        self._on_command = callback

    def player(self, name):
        player = self._post('/player', name=name)
    #   raise "#{name} isn't on the server, only found #{players.map { |p| p['name'] }}" unless player['name']
        return player

    def place_block(self, type, x, y, z):
        return self._post('/place_block', type=type, x=x, y=y, z=z)

    def nearby_entities(self, player_name, range):
        return self._post('/nearby_entities', player_name=player_name, range=range)

    def _path(self, path):
        return f'http://{self.server}:{self.port}{path}'

    def _get(self, path, **params):
        addr = self._path(path)
        if self.verbose:
            print(f"GET {addr}, {params}")
        return self._parse(requests.get(addr, params=params).content)

    def _post(self, path, **body):
        addr = self._path(path)
        if self.verbose:
            print(f"POST {addr}, {body}")
        return self._parse(requests.post(addr, json=body).content)

    def _parse(self, msg):
        try:
            return json.loads(msg)
        except Exception:
            print("Failed to parse response: %r" % msg)

    def _listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server, self.port + 1))
        sf = sock.makefile()
        print("reading from socket..")
        for line in sf.readlines():
            if self._on_command is None:
                continue
            self._on_command(json.loads(line))
        print("socket closed")
