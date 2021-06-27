import sys
sys.path.append('.')
import pycklecraft
import time

p = pycklecraft.PicklecraftClient('flarion.local', verbose=True)

# p.lift_boot()
p.set_day_time('day')

def cage(type, position):
    x, y, z = position
    p.place_blocks(type, [x-2, y, z-2], [x+2, y+2, z-2])
    p.place_blocks(type, [x-2, y, z+2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y, z-2], [x-2, y+2, z+2])
    p.place_blocks(type, [x+2, y, z-2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y+2, z-2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y-1, z-2], [x+2, y-1, z+2])


def on_command(event):
    print("event:", event)
    if event.command == "/killall":
        if event.player.name == 'jeremylightsmith':
            for player in p.players:
                if player.name != 'jeremylightsmith':
                    p.place_blocks('lava', [player.x-2, player.y-1, player.z-2], [player.x+2, player.y+2, player.z+2])
                    time.sleep(1)
                    p.place_blocks('air', [player.x-2, player.y-1, player.z-2], [player.x+2, player.y+2, player.z+2])
                    # for i in range(4):
                    #     cage('lava', player.position)
                    #     time.sleep(1)
                    #     cage('air', player.position)
                    #     time.sleep(1)

    if event.command == "/ice":
        pos = None
        while True:
            player = p.player(event.player.name)
            last_pos = None
            pos = [player.x, player.y, player.z]
            if pos != last_pos:
                p.place_blocks_in_line(
                    'ice', 
                    [pos[0], pos[1]-1, pos[2]], 
                    event.player.rotation[1], 
                    3
                )
                last_pos = pos

p.set_on_command(on_command)

print('go surf!')
p.wait_for_events()
