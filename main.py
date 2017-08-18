import thread
import threading

from input_char import getch
from walls import Permanant_Wall, Brick_Wall
from bomb import Bomb
from player import Player
from enemy import Enemy


def do_all_checks():
    
    if Enemy.all_dead():
        win()
    
    if Player.all_dead():
        lose()
    
    if Bomb.is_present()
        if bomb.exploded():
            del bomb 
            if player.position in bomb.radius:
                del player
            if enemy.position in bomb.radius:
                del enemy
            if brick_wall.position in bomb.radius:
                del brick_wall
    
    if player.position == enemy.position: #for now only one enemy, might expand on this.
        del player
        

def take_user_input(prompt, timeout=0.1):
    print prompt,    
    timer = threading.Timer(timeout, thread.interrupt_main)
    user_input = None
    try:
        timer.start()
        user_input = getch()
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return user_input

def do_all_actions(user_input):
    if user_input == 'b':
        player.drop_bomb()
    
    else if user_input in ['a','s','d','w']:
        player.move(user_input)
    else:
        pass
    
    enemy.move()

    

def each_frame():  #I need to have threading here.

    do_all_checks()
    user_input = take_user_input("")
    do_all_actions(user_input)
    Board.display()
