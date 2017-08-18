import board_object
import board
import time

class Bomb(Board_Object):
    
    Ticking_time = 5 #Change accordingly
    No_of_bombs = 0

    @staticmethod
    def is_present():
        return (No_of_bombs > 0)
           
    
    def __init__(position):
        
        Bomb.No_of_bombs +=1
        super(Bomb,self).__init__()
        self.timer = time.time()

        left = list(self.position[0]-1,self.position[1])
        right = list(self.position[0]+1,self.position[1])
        up = list(self.position[0], self.position[1]-1)
        down = list(self.position[0], self.position[1]+1)
        
        self.radius = [left,right,up,down]
        #I will add the explosion part later, and the time for which it explodes.

    def exploded(self):
        return (time.time() - self.timer() > Bomb.Ticking_time)
        

    def __del__(self):
        Bomb.No_of_bombs-=1
        board.board[self.position[0],self.position[1]] = Nothing(self.position)

    