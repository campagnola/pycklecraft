import sys
sys.path.append('.')
import pycklecraft

# p = pycklecraft.PicklecraftClient('flarion.local', verbose=True)
mc = pycklecraft.PicklecraftClient('localhost', verbose=True)

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
def on_ice(event):
    global ice_player
    player = event.player

    if ice_player == player.name:
        ice_player = None
    else:
        ice_player = player.name

@mc.on_command('/rail')
def on_iron(event):
    global rail_player
    player = event.player

    if rail_player == player.name:
        rail_player = None
    else:
        rail_player = player.name

@mc.on_command('/bats')
def on_bat(event):
    p = event.player
    for i in range(-1, 1):
        for j in range(-1, 1):
            mc.spawn_entity('bat', [p.x+i, p.y+2, p.z+j])

@mc.on_command('/spiders')
def on_bat(event):
    p = event.player
    for i in range(-1, 1):
        for j in range(-1, 1):
            mc.spawn_entity('fireball', [p.x+i, p.y+2, p.z+j])

mc.wait_for_events()
