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

@mc.on_event('player_move_event')
def on_player_move(event):
    player = event.player
    
    print(player.name, " moved ", player.position, "(ice player = ", ice_player, ")")
    if player.name == ice_player:
        mc.place_block('ice', [player.x, player.y - 1, player.z])

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
    player = event.player
    mc.place_block('iron_block', [player.x, player.y-1, player.z])

mc.wait_for_events()
