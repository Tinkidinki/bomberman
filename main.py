#--------existing utilities---------
import _thread
import threading
import os
import time
import sys

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
    sys.exit()

def lose():
    print("YOU LOSE")
    sys.exit()


def do_all_checks():
    #1
    #print(player,"do all checks")
    #global player
    #2
    #print(player, "After global")
    #print (player.position, "in do all checks")
    if Enemy.all_dead():
        win()
    
    if Player.all_dead():
        lose()
    
    if Bomb.is_present():
        bomb.timer+=1
        print("BOMB TIMER:",bomb.timer)
        if bomb.exploded():
            if player.position in bomb.radius:
                player.die()
            
            for enemy in Enemy.enemies:
                if enemy.position in bomb.radius: #i'll later extend this for multiple enemies.
                    enemy.die()
            
            for brick_wall in Brick_Wall.walls:
                if brick_wall.position in bomb.radius:
                    brick_wall.die()
        
        if bomb.explosion_over():
            bomb.die()
    #3
    #print(player)
    #global player, enemy
    #4
    #print(player)
    #global player, enemy
    for enemy in Enemy.enemies:
        if player.position == enemy.position: #for now only one enemy, might expand on this.
    #5
            print(player)
            player.move('s')
            #global player
            player.die()
        
#Try adding timed input later.
# def take_user_input(prompt, timeout=0.1):
#     print (prompt),    
#     timer = threading.Timer(timeout, _thread.interrupt_main)
#     user_input = None
#     try:
#         timer.start()
#         user_input = getch()
#     except KeyboardInterrupt:
#         pass
#     timer.cancel()
#     return user_input

def take_user_input(x):
    #return input("\n")
    return getch()

def do_all_actions(user_input):

    if user_input == 'b':
        if not(Bomb.is_present()):
            player.drop_bomb()
    
    elif user_input in ['a','s','d','w']:
        player.move(user_input)
    else:
        pass
    
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def each_frame():  #I need to have threading here.
    
    #print (player.position)
    for enemy in Enemy.enemies:
        enemy.move()
    #print(player.position,"player position AFTER ENEMY BEFORE PLAYER")
    #print(enemy.position, "enemy position AFTER ENEMY BEFORE PLAYER")
    print("No. of enemies after enemy move", Enemy.No_of_enemies)
    do_all_checks()
    board.display()
    #board.display_objects()
    user_input = take_user_input("")
    do_all_actions(user_input)
    #print(player.position, "player position AFTER PLAYER")
    #print(enemy.position, "enemy position AFTER PLAYER")
    do_all_checks()
    board.display()
    #board.display_objects()
    print("No. of enemies after player", Enemy.No_of_enemies)
    
    
    print("No. of enemies after player and checks", Enemy.No_of_enemies)
    #time.sleep(1)
    #clear_screen()
