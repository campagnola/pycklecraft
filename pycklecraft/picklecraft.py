import queue
import json
import socket
import requests
import threading
import math
from .player import Player


class PicklecraftClient:
    def __init__(self, server='localhost', port=3200, verbose=False):
        self.verbose = verbose
        self.server = server
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.port))

        self.result_queue = queue.Queue()

        self.listen_thread = threading.Thread(target=self._listen, daemon=True)
        self.listen_thread.start()

    @property
    def players(self):
        return [Player(p) for p in self._rpc(method='getPlayers')]

    def set_on_command(self, callback):
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

    def place_blocks_in_line(self, type, position, rotation, length):
        for i in range(length):
            position = self._increment_position_in_direction(position,
                                                             rotation,
                                                             1)
            self._rpc(method='placeBlock',
                      type=type,
                      position=[math.floor(position[0]),
                                math.floor(position[1]),
                                math.floor(position[2])])

    def get_blocks(self, fromPos, toPos):
        return self._rpc(method='getBlocks', fromPosition=fromPos, toPosition=toPos)

    def nearby_entities(self, player_name, range):
        return self._rpc(method='getNearbyEntities', playerName=player_name, range=range)

    def set_day_time(self, time):
        return self._rpc(method='setDayTime', time=time)

    def lift_boot(self):
        return self._rpc(method='liftBoot')

    def _increment_position_in_direction(self, position, rotation, distance):
        return [
            position[0] - distance * math.sin(math.radians(rotation)),
            position[1],
            position[2] + distance * math.cos(math.radians(rotation)),
        ]

    def _rpc(self, **args):
        self.sock.send(json.dumps(args).encode() + b'\n')
        result = self.result_queue.get()
        if result['status'] == 'OK':
            return result['result']
        else:
            raise Exception(result['error'])

    # def _path(self, path):
    #     return f'http://{self.server}:{self.port}{path}'

    # def _rpc(self, **body):
    #     addr = self._path('/rpc')
    #     if self.verbose:
    #         print(f"POST {addr}, {body}")
    #     response = requests.post(addr, json=body)
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         raise Exception(response.text)

    def _parse(self, msg):
        try:
            return json.loads(msg)
        except Exception:
            print("Failed to parse response: %r" % msg)

    def _listen(self):
        print("reading from " + self.server + ":" + str(self.port + 1) + "...")
        try:
            while True:
                line = self.sock.recv(4096).decode('UTF-8')
                if self.verbose:
                    print("read: " + line)

                if line == '':
                    raise Exception("remote end hung up")
                data = json.loads(line)
                if 'status' in data:
                    self.result_queue.put(data)
                elif self._on_command is not None:
                    self._on_command(data)
        except Exception:
            print("closing socket")
            self.sock.close()
            raise
