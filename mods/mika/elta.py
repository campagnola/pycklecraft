import sys
sys.path.append('.')
import pycklecraft
import math

p = pycklecraft.PicklecraftClient('flarion.local', verbose=True)

p.set_day_time('day')

def cage(type, position):
    x, y, z = position
    p.place_blocks(type, [x-2, y, z-2], [x+2, y+2, z-2])
    p.place_blocks(type, [x-2, y, z+2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y, z-2], [x-2, y+2, z+2])
    p.place_blocks(type, [x+2, y, z-2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y+2, z-2], [x+2, y+2, z+2])

def place_blocks_in_line(self, type, position, rotation, start, stop):
    for i in range(start, stop):
        position = self._increment_position_in_direction(position,
                                                            rotation,
                                                            1)
        self._rpc(method='placeBlock',
                    type=type,
                    position=[math.floor(position[0]),
                            math.floor(position[1]),
                            math.floor(position[2])])

def on_command(event):
    print("event:", event)
    player = event.player
    if event.command == "/earth":
        place_blocks_in_line(
            p,
            'cobblestone', 
            [player.x, player.y-1, player.z],
            player.rotation[1], 
            1,
            100
        )
    elif event.command == "/fire":
        place_blocks_in_line(
            p,
            'lava', 
            [player.x, player.y-1, player.z], 
            player.rotation[1], 
            1,
            100
        )
    elif event.command == "/water":
        place_blocks_in_line(
            p,
            'water', 
            [player.x, player.y, player.z], 
            player.rotation[1], 
            1,
            100
        )

    elif event.command == "/aero_o_air":
        place_blocks_in_line(
            p,
            'air', 
            [player.x, player.y, player.z], 
            player.rotation[1], 
            1,
            100
        )

    elif event.command == "/ball_o_air":
        p.place_blocks('air', 
                       [player.x+20, player.y+20, player.z+20], 
                       [player.x-20, player.y, player.z-20])

p.set_on_command(on_command)

print('cages are ready!')
p.wait_for_events()



        
