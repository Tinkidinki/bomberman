import board
#Every object on the board will come under this class.
#Position is an [x,y] list.
#Position[0] is x coordinate, Position[1] is y coordinate

class Board_Object:
    def __init__(position):
        self.position = position
        Board.board[self.position[0],self.position[1]] = self



        

    
