import sys
sys.path.append('.')
import pycklecraft
import threading

p = pycklecraft.PicklecraftClient('flarion.local', verbose=True)

p.set_day_time('day')

def cage(type, position):
    x, y, z = position
    p.place_blocks(type, [x-2, y, z-2], [x+2, y+2, z-2])
    p.place_blocks(type, [x-2, y, z+2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y, z-2], [x-2, y+2, z+2])
    p.place_blocks(type, [x+2, y, z-2], [x+2, y+2, z+2])
    p.place_blocks(type, [x-2, y+2, z-2], [x+2, y+2, z+2])

tunta_running = False
tunta_player = None

def tunta_run():
    while True:
        if tunta_running:
            player = p.player(tunta_player.name)
            p.place_block('redstone_block', 
                    [player.x,player.y - 1,player.z])

def on_command(event):
    global tunta_player
    global tunta_running
    print("event:", event)
    if event.command == "/cage":
        cage('diamond_block', event.player.position)
    
    elif event.command == "/uncage":
        cage('air', event.player.position)

    elif event.command == "/rock":
        p.place_blocks_in_line(
            'cobblestone', 
            event.player.position, 
            event.player.rotation[1], 
            20
        )

    elif event.command == "/red":
        tunta_player = event.player
        tunta_running = True






    elif event.command == "/redd":
        tunta_running = False







p.set_on_command(on_command)

threading.Thread(target=tunta_run, daemon=True).start()

print('cages are ready!')
p.wait_for_events()



