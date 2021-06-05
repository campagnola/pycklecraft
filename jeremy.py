import pycklecraft
import pycklecraft

p = pycklecraft.PicklecraftClient('localhost', verbose=True)

# players = p.players
# print("Players:")
# for player in players:
#     print(player.name)
# player = players[0]

# p.lift_boot()
p.set_day_time('day')
# print("First player:", p.player(player.name).data)

# print("Entities:", p.nearby_entities(player.name, 50))

# p.place_block('grass', [player.x, player.y, player.z])


def on_command(cmd):
    print("CMD:", cmd)


p.set_on_command(on_command)

p.wait_for_events()
