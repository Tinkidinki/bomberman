from board_object import Board_Object
from board import Board
from nothing import Nothing
import random

class Enemy(Board_Object):
    
    No_of_enemies = 0
    enemies = []

    @staticmethod
    def all_dead():
        #print("IN ALL DEAD FUNCTION", Enemy.No_of_enemies)
        if Enemy.No_of_enemies == 0:
            return True
        else:
            return False
    
    def __init__(self):
        Enemy.No_of_enemies+=1
        super(Enemy,self).__init__()
        self.alive = True
        Enemy.enemies.append(self)
        #print ("Enemy object was created")
    
    def move(self):
        left = [self.position[0],self.position[1]-1]
        right = [self.position[0],self.position[1]+1]
        up = [self.position[0]-1, self.position[1]]
        down = [self.position[0]+1, self.position[1]]
        
        possible_new_positions = [left, right, up, down]
        #d
        #print(possible_new_positions,"possible_new_positions")

        choices = []
        for position in possible_new_positions:
            #print(position,"position enemy")
            #print(board.is_within_board(position),"whether its within board")
            if board.is_within_board(position) and board.is_empty(position):
                choices.append(position)
        #print(choices,end="choices\n")
        
        if choices != []:
            board.board[self.position[0]][self.position[1]] = Nothing()
            self.position = random.choice(choices)
            board.board[self.position[0]][self.position[1]] = self
    
    def die(self):
        Enemy.No_of_enemies -=1
        Enemy.enemies.remove(self)
        board.board[self.position[0]][self.position[1]] = Nothing()
        player.score+=100
        self.alive = False
