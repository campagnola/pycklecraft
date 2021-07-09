import sys
import threading
sys.path.append('.')
import pycklecraft
import time
import traceback

mc = pycklecraft.PicklecraftClient('flarion.local', verbose=True)

# players = mc.players
# print("Players:")
# for player in players:
#     print(player.name)
# player = players[0]

mc.lift_boot()
mc.set_day_time('day')
# print("First player:", mc.player(player.name).data)

# print("Entities:", mc.nearby_entities(player.name, 50))

# mc.place_block('grass', [player.x, player.y, player.z])

# player = mc.player('jeremylightsmith')
# mc.place_block('ice', [player.x, player.y - 1, player.z])

ice_player = None
rail_player = None

@mc.on_event('player_move_event')
def on_player_move(event):
    player = event.player
    
    if player.name == ice_player:
        mc.place_block('ice', [player.x, player.y - 1, player.z])

    elif player.name == rail_player:
        mc.place_block('rail', [player.x, player.y, player.z])

@mc.on_command('/ice')
def on_ice(player, command):
    global ice_player

    if ice_player == player.name:
        ice_player = None
    else:
        ice_player = player.name

@mc.on_command('/rail')
def on_iron(player, command):
    global rail_player

    if rail_player == player.name:
        rail_player = None
    else:
        rail_player = player.name

fireball_target = None
fireball_pos = None

@mc.on_command('/fireball')
def shoot_fireball(player, command):
    global fireball_target
    global fireball_pos

    fireball_target = command.split(' ')[1]
    fireball_pos = [player.x, player.y + 2, player.z]
    mc.place_block('lava', fireball_pos)

@mc.on_command('/bats')
def on_bat(p, command):
    for i in range(-1, 1):
        for j in range(-1, 1):
            mc.spawn_entity('bat', [p.x+i, p.y+2, p.z+j])

@mc.on_command('/spiders')
def on_bat(p, command):
    for i in range(-1, 1):
        for j in range(-1, 1):
            mc.spawn_entity('fireball', [p.x+i, p.y+2, p.z+j])

def approach_num(n, target, incr):
    if n == target:
        return n
    elif target > n:
        return min(target, n + incr)
    else:
        return max(target, n - incr)

def approach_point(p, target, incr):
    return [
        approach_num(p[0], target[0], incr),
        approach_num(p[1], target[1], incr),
        approach_num(p[2], target[2], incr),
    ]

def fireball_tracking():
    global fireball_target
    global fireball_pos

    while True:
        try:
            if fireball_target:
                player = mc.player(fireball_target)
                target = [player.x, player.y, player.z]
                print("fireball_pos", fireball_pos)
                print("target", target)
                next_pos = approach_point(fireball_pos, target, 2)

                if fireball_pos == next_pos:
                    print("done!")
                    fireball_target = None
                else:
                    print("next_pos", next_pos)
                    mc.place_block('lava', next_pos)
                    mc.place_block('air', fireball_pos)
                    fireball_pos = next_pos
                    time.sleep(0.1)

            else:
                time.sleep(1)
        except:
            traceback.print_exc()

threading.Thread(target=fireball_tracking, daemon=True).start()

mc.wait_for_events()
