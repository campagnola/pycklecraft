import pycklecraft
import sys
import pycklecraft

p = pycklecraft.PicklecraftClient('localhost', verbose=True)

print("Players:", p.players)

name = p.players[0]['name']
print("First player:", p.player(name))

print("Entities:", p.nearby_entities(name, 50))

p.place_block('grass', 0, 0, 0)


def on_command(cmd):
    print("CMD:", cmd)


p.set_on_command(on_command)
