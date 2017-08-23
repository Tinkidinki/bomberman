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
        #print("IN THE BOMB INIT METHOD ",self.position)
        Bomb.No_of_bombs +=1

        self.timer = 0
        print("DEBUGGING LIST INDEX OUT OF RANGE")
        print(self.position[0],self.position[1])
        left = [self.position[0],self.position[1]-1]
        right = [self.position[0],self.position[1]+1]
        up = [self.position[0]-1, self.position[1]]
        down = [self.position[0]+1, self.position[1]]
        
        self.radius = [left,right,up,down,self.position]
        #I will add the explosion part later, and the time for which it explodes.

    def exploded(self):
        return (self.timer > Bomb.Ticking_time)

    def explosion_over(self):
        return (self.timer > Bomb.Ticking_time + Bomb.Exploding_time)
        

    def die(self):
        Bomb.No_of_bombs-=1
        board.board[self.position[0]][self.position[1]] = Nothing()


    