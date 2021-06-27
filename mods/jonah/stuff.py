import sys
sys.path.append('.')
import pycklecraft
import threading

mc = pycklecraft.PicklecraftClient('flarion.local', verbose=True)

mc.set_day_time('day')

def cage(type, position):
    x, y, z = position
    mc.place_blocks(type, [x-2, y, z-2], [x+2, y+2, z-2])
    mc.place_blocks(type, [x-2, y, z+2], [x+2, y+2, z+2])
    mc.place_blocks(type, [x-2, y, z-2], [x-2, y+2, z+2])
    mc.place_blocks(type, [x+2, y, z-2], [x+2, y+2, z+2])
    mc.place_blocks(type, [x-2, y+2, z-2], [x+2, y+2, z+2])

tunta_running = False
tunta_player = None

@mc.on_event('player_move_event')
def on_player_move(event):
    player = event.player
    if tunta_running and player.name == tunta_player:
        mc.place_block('redstone_block', [player.x,player.y - 1,player.z])

@mc.on_command('/cage')
def on_cage(player, command):
    cage('diamond_block', player.position)

@mc.on_command('/uncage')
def on_uncage(player, command):
    cage('air', player.position)

@mc.on_command('/rock')
def on_rock(player, command):
    mc.place_blocks_in_line(
        'cobblestone', 
        player.position, 
        player.rotation[1], 
        20
    )

@mc.on_command('/red')
def start_red(player, command):
    global tunta_player
    global tunta_running
    
    tunta_player = player
    tunta_running = True

@mc.on_command('/redd')
def stop_red(player, command):
    global tunta_running

    tunta_running = False

mc.wait_for_events()
