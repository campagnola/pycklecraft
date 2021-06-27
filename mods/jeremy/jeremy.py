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

ice_player = None

def on_event(event):
    global ice_player
    player = event.player
    
    if event.type == 'player_move_event':
        if player.name == ice_player:
            p.place_block('ice', [player.x, player.y - 1, player.z])

    elif event.type == 'command_event':
        print("command: ", event.data)
        if event.command == '/jump':
            p.move_player(player.name, [player.x + 1, player.y, player.z])
        
        elif event.command == '/ice':
            if ice_player == player.name:
                ice_player = None
            else:
                ice_player = player.name
p.set_on_command(on_event)

@p.on_player_move
def on_player_move(event):


p.wait_for_events()
