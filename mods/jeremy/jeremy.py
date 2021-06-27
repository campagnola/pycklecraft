import sys
sys.path.append('.')
import pycklecraft

# p = pycklecraft.PicklecraftClient('flarion.local', verbose=True)
p = pycklecraft.PicklecraftClient('localhost', verbose=True)

# players = p.players
# print("Players:")
# for player in players:
#     print(player.name)
# player = players[0]

p.lift_boot()
p.set_day_time('day')
# print("First player:", p.player(player.name).data)

# print("Entities:", p.nearby_entities(player.name, 50))

# p.place_block('grass', [player.x, player.y, player.z])

# player = p.player('jeremylightsmith')
# p.place_block('ice', [player.x, player.y - 1, player.z])

ice_player = None

@p.on_event('player_move_event')
def on_player_move(event):
    player = event.player
    
    print(player.name, " moved ", player.position, "(ice player = ", ice_player, ")")
    if player.name == ice_player:
        p.place_block('ice', [player.x, player.y - 1, player.z])

@p.on_command('/ice')
def on_ice(event):
    global ice_player
    player = event.player

    if ice_player == player.name:
        ice_player = None
    else:
        ice_player = player.name

@p.on_command('/iron')
def on_iron(event):
    player = event.player
    p.place_block('iron_block', [player.x, player.y-1, player.z])

p.wait_for_events()
