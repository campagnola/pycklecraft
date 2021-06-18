import sys
sys.path.append('.')
import pycklecraft

p = pycklecraft.PicklecraftClient('flarion.local', verbose=True)

p.lift_boot()
p.set_day_time('day')

def cage(type, position):
    x, y, z = position
    p.place_blocks(type, [x-2, y, z-2], [x+2, y+2, z-2])
    p.place_blocks(type, [x-2, y, z+2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y, z-2], [x-2, y+2, z+2])
    p.place_blocks(type, [x+2, y, z-2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y+2, z-2], [x+2, y+2, z+2])


player = p.player('jeremylightsmith')


def on_command(event):
    print("event:", event)
    if event.command == "/cage":
        cage('glass', event.player.position)

    elif event.command == "/rock":
        p.place_blocks_in_line(
            'cobblestone', 
            event.player.position, 
            event.player.rotation[1], 
            20
        )

p.set_on_command(on_command)

print('cages are ready!')
p.wait_for_events()
