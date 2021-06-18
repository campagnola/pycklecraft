import sys
import pycklecraft

cli = pycklecraft.PicklecraftClient(sys.argv[1], verbose=True)

print("Players:", cli.players)

name = cli.players[0].name
print("First player:", cli.player(name))

print("Entities:", cli.nearby_entities(name, 50))

cli.place_block('grass', (0, 0, 0))

def on_command(cmd):
    print("CMD:", cmd)

cli.set_on_command(on_command)
