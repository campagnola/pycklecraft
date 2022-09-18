import sys
sys.path.append('.')
import pycklecraft
import math

mc = pycklecraft.PicklecraftClient('localhost', verbose=True)

mc.set_day_time('day')

def cage(type, position):
    x, y, z = position
    mc.place_blocks(type, [x-2, y, z-2], [x+2, y+2, z-2])
    mc.place_blocks(type, [x-2, y, z+2], [x+2, y+2, z+2])
    mc.place_blocks(type, [x-2, y, z-2], [x-2, y+2, z+2])
    mc.place_blocks(type, [x+2, y, z-2], [x+2, y+2, z+2])
    mc.place_blocks(type, [x-2, y+2, z-2], [x+2, y+2, z+2])

def place_blocks_in_line(type, position, rotation, start, stop):
    for i in range(start, stop):
        position = mc.increment_position_in_direction(position,
                                                      rotation,
                                                      1)
        mc._rpc(method='placeBlock',
                    type=type,
                    position=[math.floor(position[0]),
                            math.floor(position[1]),
                            math.floor(position[2])])

@mc.on_command('earth')
def on_earth(player, command):
    place_blocks_in_line(
        'cobblestone', 
        [player.x, player.y-1, player.z],
        player.rotation[1], 
        1,
        100
    )

@mc.on_command('fire')
def on_fire(player, command):
    place_blocks_in_line(
        'lava', 
        [player.x, player.y-1, player.z], 
        player.rotation[1], 
        1,
        100
    )

@mc.on_command('aaaaahhh')
def on_aaaaahhh(player, command):
    mc.spawn_entity('spider', [player.x, player.y-1, player.z])
    mc.spawn_entity('spider', [player.x, player.y-1, player.z])
    mc.spawn_entity('skeleton', [player.x, player.y-1, player.z])
    mc.spawn_entity('skeleton', [player.x, player.y-1, player.z])
    mc.spawn_entity('creeper', [player.x, player.y-1, player.z])
    mc.spawn_entity('creeper', [player.x, player.y-1, player.z])
    mc.spawn_entity('zombie', [player.x, player.y-1, player.z])
    mc.spawn_entity('zombie', [player.x, player.y-1, player.z])



@mc.on_command('backup')
def on_backup(player, command):

    mc.spawn_entity('shulker', [player.x, player.y-1, player.z])
    mc.spawn_entity('shulker', [player.x, player.y-1, player.z])
    mc.spawn_entity('shulker', [player.x, player.y-1, player.z])
    mc.spawn_entity('shulker', [player.x, player.y-1, player.z])


@mc.on_command('aaaaahhhnether')
def on_aaaaahhhnether(player, command):
    mc.spawn_entity('wither_skeleton', [player.x, player.y-1, player.z])
    mc.spawn_entity('wither_skeleton', [player.x, player.y-1, player.z])
    mc.spawn_entity('ghast', [player.x, player.y-1, player.z])
    mc.spawn_entity('ghast', [player.x, player.y-1, player.z])
    mc.spawn_entity('blaze', [player.x, player.y-1, player.z])
    mc.spawn_entity('blaze', [player.x, player.y-1, player.z])
    mc.spawn_entity('wither', [player.x, player.y-1, player.z])
    mc.spawn_entity('wither', [player.x, player.y-1, player.z])


@mc.on_command('aaaaahhhend')
def on_aaaaahhhnend(player, command):
    mc.spawn_entity('enderman', [player.x, player.y-1, player.z])
    mc.spawn_entity('enderman', [player.x, player.y-1, player.z])
    mc.spawn_entity('endermite', [player.x, player.y-1, player.z])
    mc.spawn_entity('endermite', [player.x, player.y-1, player.z])
    mc.spawn_entity('shulker', [player.x, player.y-1, player.z])
    mc.spawn_entity('shulker', [player.x, player.y-1, player.z])
    mc.spawn_entity('ender_dragon', [player.x, player.y-1, player.z])
    mc.spawn_entity('ender_dragon', [player.x, player.y-1, player.z])



@mc.on_command('water')
def on_water(player, command):
    place_blocks_in_line(
        'water', 
        [player.x, player.y, player.z], 
        player.rotation[1], 
        1,
        100
    )

@mc.on_command('aero_o_air')
def on_aero_o_air(player, command):
    place_blocks_in_line(
        'air', 
        [player.x, player.y, player.z], 
        player.rotation[1], 
        1,
        100
    )

@mc.on_command('ball_o_air')
def on_ball_o_air(player, command):
    mc.place_blocks('air', 
                    [player.x+20, player.y+20, player.z+20], 
                    [player.x-20, player.y, player.z-20])

air_player = None

@mc.on_command('air')
def air(player, command):
    global air_player
    air_player = player

@mc.on_event('player_move_event')
def on_player_move(event):
    if air_player and air_player.name == event.player.name:
        player = event.player
        
        print(player.name, " moved to ", player.position)
        mc.place_blocks('air', [player.x-1, player.y, player.z-1], [player.x+1, player.y+1, player.z+1])

@mc.on_command('rock')
def rock(player, command):
    print("I am the rock")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        5)
    pyramid(pos, "ancient_debris")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        13)
    pyramid(pos, "ancient_debris")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        21)
    pyramid(pos, "ancient_debris")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        29)
    pyramid(pos, "ancient_debris")

@mc.on_command('volcano')
def volcano(player, command):
    print("I am the rock")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        5)
    pyramid(pos, "lava")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        13)
    pyramid(pos, "lava")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        21)
    pyramid(pos, "lava")
    pos = mc.increment_position_in_direction(
        player.position, 
        player.rotation[1], 
        29)
    pyramid(pos, "lava")


def pyramid(pos, tip_type):
    x, y, z = pos[0], pos[1], pos[2]

    mc.place_block('ancient_debris', [x, y, z])
    mc.place_block('ancient_debris', [x, y, z+1])
    mc.place_block('ancient_debris', [x, y, z+2])
    mc.place_block('ancient_debris', [x, y, z-1])
    mc.place_block('ancient_debris', [x, y, z-2])
    mc.place_block('ancient_debris', [x+1, y, z])
    mc.place_block('ancient_debris', [x+2, y, z])
    mc.place_block('ancient_debris', [x-1, y, z])
    mc.place_block('ancient_debris', [x-2, y, z])
    mc.place_block('ancient_debris', [x-1, y, z-1])
    mc.place_block('ancient_debris', [x+1, y, z+1])
    mc.place_block('ancient_debris', [x+1, y, z-1])
    mc.place_block('ancient_debris', [x-1, y, z+1])

    mc.place_block('ancient_debris', [x, y+1, z])
    mc.place_block('ancient_debris', [x, y+1, z+1])
    mc.place_block('ancient_debris', [x, y+1, z-1])
    mc.place_block('ancient_debris', [x+1, y+1, z])
    mc.place_block('ancient_debris', [x-1, y+1, z])
    mc.place_block('ancient_debris', [x-1, y+1, z-1])
    mc.place_block('ancient_debris', [x+1, y+1, z+1])
    mc.place_block('ancient_debris', [x+1, y+1, z-1])
    mc.place_block('ancient_debris', [x-1, y+1, z+1])

    mc.place_block('ancient_debris', [x, y+2, z])
    mc.place_block('ancient_debris', [x, y+2, z+1])
    mc.place_block('ancient_debris', [x, y+2, z-1])
    mc.place_block('ancient_debris', [x+1, y+2, z])
    mc.place_block('ancient_debris', [x-1, y+2, z])

    mc.place_block(tip_type, [x, y+3, z])







mc.wait_for_events()

