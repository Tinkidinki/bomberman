#--------existing utilities---------
import _thread
import threading
import os

#--------created utilities----------
# from input_char import getch

#--------entities-------------------
# from board_object import Board_Object
# from walls import Permanant_Wall, Brick_Wall
# from bomb import Bomb
# from player import Player
# from enemy import Enemy
# from nothing import Nothing

#----------------------------------

def win():
    print("YOU WIN")
    exit()

def lose():
    print("YOU LOSE")
    exit()


def do_all_checks():
    
    global player
    print (player.position, "in do all checks")
    if Enemy.all_dead():
        win()
    
    if Player.all_dead():
        lose()
    
    if Bomb.is_present():
        if bomb.exploded():
            if player.position in bomb.radius:
                del player
            if enemy.position in bomb.radius:
                del enemy
            if brick_wall.position in bomb.radius:
                del brick_wall
        
        if bomb.explosion_over():
            del bomb

    global player, enemy
    if player.position == enemy.position: #for now only one enemy, might expand on this.
        del player
        

def take_user_input(prompt, timeout=0.1):
    print (prompt),    
    timer = threading.Timer(timeout, _thread.interrupt_main)
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
    
    elif user_input in ['a','s','d','w']:
        player.move(user_input)
    else:
        pass
    
    enemy.move()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def each_frame():  #I need to have threading here.

    print (player.position)
    do_all_checks()
    user_input = take_user_input("")
    do_all_actions(user_input)
    board.display()
    clear_screen()
