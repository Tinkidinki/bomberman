import board_object
import board
import random

class Enemy(Board_Object):
    
    No_of_enemies = 0

    @staticmethod
    def all_dead():
        if Enemy.No_of_enemies == 0:
            return True
        else:
            return False
    
    def __init__(self, position):
        No_of_enemies+=1
        super(Enemy,self).__init__(position)
    
    def move(self):
        left = list(self.position[0]-1,self.position[1])
        right = list(self.position[0]+1,self.position[1])
        up = list(self.position[0], self.position[1]-1)
        down = list(self.position[0], self.position[1]+1)
        
        possible_new_positions = [left, right, up, down]

        choices = []
        for position in possible_new_positions:
            if board.is_within_board(possible_new_position) and board.is_empty(possible_new_position):
                choices.append(position)
        
        self.position = random.choice(choices)

        

    
    def __del__(self)
        Enemy.No_of_enemies -=1
        board.board[self.position[0],self.position[1]] = Nothing(self.position)
