from board_object import Board_Object
from board import Board
import random

class Enemy(Board_Object):
    
    No_of_enemies = 0

    @staticmethod
    def all_dead():
        if Enemy.No_of_enemies == 0:
            return True
        else:
            return False
    
    def __init__(self):
        Enemy.No_of_enemies+=1
        super(Enemy,self).__init__()
    
    def move(self):
        left = [self.position[0]-1,self.position[1]]
        right = [self.position[0]+1,self.position[1]]
        up = [self.position[0], self.position[1]-1]
        down = [self.position[0], self.position[1]+1]
        
        possible_new_positions = [left, right, up, down]
        #d
        print(possible_new_positions,"possible_new_positions")

        choices = []
        for position in possible_new_positions:
            print(board.is_within_board(position))
            print(board.is_empty(position))
            if board.is_within_board(position) and board.is_empty(position):
                choices.append(position)
        print(choices,end="choices")
        
        self.position = random.choice(choices)

        

    
    def __del__(self):
        Enemy.No_of_enemies -=1
        board.board[self.position[0]][self.position[1]] = Nothing()
