#--------existing utilities---------
import sys
import _thread
import threading
import os
import time


# --------created utilities----------
# from input_char import getch
from asynchronous_input import get_char_keyboard_nonblock


def lose():
    print("YOU LOSE")
    print("YOUR LAST LEVEL SCORE", player.score)
    sys.exit()

# ----------------ALL THE CHECKS------------------------------
def do_all_checks():
    
    if Enemy.all_dead():
        level_up()
        
    if Player.all_dead():
        lose()
        
    if Bomb.is_present():
        bomb.timer += 1
        if bomb.exploded():
            if player.position in bomb.radius:
                player.die()
                
            for enemy in Enemy.enemies:
                if enemy.position in bomb.radius:
                    enemy.die()
                
            for brick_wall in Brick_Wall.walls:
                if brick_wall.position in bomb.radius:
                    brick_wall.die()
    
        if bomb.explosion_over():
                bomb.die()
   
    for enemy in Enemy.enemies:
        if player.position == enemy.position:
            player.die()
        
# --------------------------------------------------------------


def take_user_input(x):
    return get_char_keyboard_nonblock()


def do_all_actions(user_input):

    if user_input == 'b':
        if not Bomb.is_present():
            player.drop_bomb()

    elif user_input in ['a', 's', 'd', 'w']:
        player.move(user_input)

    elif user_input == 'q':
        sys.exit()

    else:
        pass


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def each_frame():
    do_all_checks()
    board.big_display()
    time.sleep(0.3)
    #clear_screen()


def main(): 
    # --------ENEMY PORTION---------------
    for enemy in Enemy.enemies:
        enemy.move()
    
    each_frame()

    # -----------PLAYER PORTION------------
    user_input = take_user_input("")
    do_all_actions(user_input)

    each_frame()
