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
        return self._rpc(method='getPlayers')

    def set_on_command(self, callback):
        self._on_command = callback

    def player(self, name):
        player = self._rpc(method='getPlayer', name=name)
        return player

    def place_block(self, type, x, y, z):
        return self._rpc(method='placeBlock', type=type, x=x, y=y, z=z)

    def nearby_entities(self, player_name, range):
        return self._rpc(method='nearbyEntities', player_name=player_name, range=range)

    def set_day_time(self, time):
        return self._rpc(method='setDayTime', time=time)

    def lift_boot(self):
        return self._rpc(method='liftBoot')

    def _path(self, path):
        return f'http://{self.server}:{self.port}{path}'

    def _rpc(self, **body):
        addr = self._path('/rpc')
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
