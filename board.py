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
        return (position[0]>=0 and position[0] < self.dimensions[0] and position[1]>=0 and position[1]<self.dimensions[1])

    def is_empty(self, position):
        #print(self.board[position[0]][position[1]])
        return (isinstance(self.board[position[0]][position[1]],Nothing) or isinstance(self.board[position[0]][position[1]],Player) or isinstance(self.board[position[0]][position[1]],Enemy))

    def display(self): #I will convert this to the right size later
        symbol =   {Permanant_Wall:"#", Brick_Wall:"/",Player: "B",Enemy: "E", Bomb:"O", Nothing:" ", "explosion":"e"}
        #make explosion also happen
        to_print = [["" for x in range(self.dimensions[0])] for j in range(self.dimensions[1])]
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                to_print[i][j] = symbol[type(self.board[i][j])] 
        
        if Bomb.is_present():
            if bomb.exploded():
                for radius in bomb.radius:
                    if (board.is_within_board(radius)):
                        to_print[radius[0]][radius[1]] = symbol["explosion"]

        print('X'*(self.dimensions[1]+2))
        for i in range(self.dimensions[0]):
            print('X',end="")
            for j in range(self.dimensions[1]):
                print (to_print[i][j], end = "")
            print('X',end="")
            print()
        print('X'*(self.dimensions[1]+2))

    def update_positions(self):
        #board.display_objects()
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                #print("tuple",i,j)
                (self.board[i][j]).position = [i,j]       

    #debugging purposes
    def display_objects(self):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                print (self.board[i][j] , end = "")
            print()
