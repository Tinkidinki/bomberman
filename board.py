from walls import Permanant_Wall

class Board():
    
    def __init__(self,board,dimensions):
        #board is a 2d array initialised with objects.
        #The initial config depends on the level
        self.board = board
        
        #dimesions is a 2-list with number of x and number of y
        #I'm using 0-numbering for the board
        self.dimensions = dimensions
    
    def is_within_board(self, position):
        return (position[0]>=0 and position[0] <= self.dimensions[0] and position[1]>=0 and position[1]<=self.dimensions[1])

    def is_empty(self, position):
        return (isinstance(self.board[position[0]][position[1]],Nothing))

    def display(self): #I will convert this to the right size later
        symbol =   {Permanant_Wall:"#", Brick_Wall:"/",Player: "B",Enemy: "E", Bomb:"O", Nothing:" "}
        #make explosion also happen
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                print (symbol[type(self.board[i][j])] , end = "")
            print()

    def update_positions(self):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                self.board[i][j].position = [i,j]       