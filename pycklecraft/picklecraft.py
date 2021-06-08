import json
import socket
import requests
import threading
from .player import Player


class PicklecraftClient:
    def __init__(self, server='localhost', port=3200, verbose=False):
        self.verbose = verbose
        self.server = server
        self.port = port

    @property
    def players(self):
        return [Player(p) for p in self._rpc(method='getPlayers')]

    def set_on_command(self, callback):
        self.listen_thread = threading.Thread(target=self._listen, daemon=True)
        self.listen_thread.start()

        self._on_command = None
        self._on_command = callback

    def wait_for_events(self):
        try:
            self.listen_thread.join()
        except:
            None  # this is okay, we just got a SIGINT

    def player(self, name):
        return Player(self._rpc(method='getPlayer', name=name))

    def place_block(self, type, position):
        return self._rpc(method='placeBlock', type=type, position=position)

    def place_blocks(self, type, fromPos, toPos):
        return self._rpc(method='placeBlocks', type=type, fromPosition=fromPos, toPosition=toPos)

    def get_blocks(self, fromPos, toPos):
        return self._rpc(method='getBlocks', fromPosition=fromPos, toPosition=toPos)

    def nearby_entities(self, player_name, range):
        return self._rpc(method='getNearbyEntities', playerName=player_name, range=range)

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
        response = requests.post(addr, json=body)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.text)

    def _parse(self, msg):
        try:
            return json.loads(msg)
        except Exception:
            print("Failed to parse response: %r" % msg)

    def _listen(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.port + 1))
        print("reading from " + self.server + ":" + str(self.port + 1) + "...")
        try:
            while True:
                line = self.sock.recv(4096).decode('UTF-8')
                if self.verbose:
                    print("read: " + line)
                if self._on_command is None:
                    continue
                self._on_command(json.loads(line))
        except:
            print("closing socket")
            self.sock.close()
