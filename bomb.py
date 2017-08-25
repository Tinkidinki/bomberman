from board_object import Board_Object
from board import Board
import time

class Bomb(Board_Object):
    
    Ticking_time = 5 #Change accordingly
    Exploding_time = 3
    No_of_bombs = 0

    @staticmethod
    def is_present():
        return (Bomb.No_of_bombs > 0)
           
    
    def __init__(self,position):
        super(Bomb,self).__init__()
        self.position = position
        board.board[self.position[0]][self.position[1]] = self
        Bomb.No_of_bombs += 1

        self.timer = 0
        left = [self.position[0],self.position[1]-1]
        right = [self.position[0],self.position[1]+1]
        up = [self.position[0]-1, self.position[1]]
        down = [self.position[0]+1, self.position[1]]
        
        self.radius = [left,right,up,down]


    def exploded(self):
        return (self.timer > Bomb.Ticking_time)


    def explosion_over(self):
        return (self.timer > Bomb.Ticking_time + Bomb.Exploding_time)


    def display(self):
        if (Bomb.Ticking_time >= self.timer):
            return str(Bomb.Ticking_time - self.timer)
        else:
            return str(0)
        

    def die(self):
        Bomb.No_of_bombs -= 1
        board.board[self.position[0]][self.position[1]] = Nothing()


    