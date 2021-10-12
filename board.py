from walls import Permanant_Wall

class Board():

    def __init__(self, board, dimensions):
        self.board = board
        self.dimensions = dimensions

    def is_within_board(self, position):
        return (position[0] >= 0 and position[0] < self.dimensions[0] 
                and position[1] >= 0 and position[1] < self.dimensions[1])

    def is_bombable(self, position):
        return isinstance(self.board[position[0]][position[1]],Nothing) or isinstance(self.board[position[0]][position[1]],Player) or isinstance(self.board[position[0]][position[1]],Enemy) or isinstance(self.board[position[0]][position[1]],Brick_Wall)

    def is_empty(self, position):
        return isinstance(self.board[position[0]][position[1]],Nothing) or isinstance(self.board[position[0]][position[1]],Player) or isinstance(self.board[position[0]][position[1]],Enemy) 



    def big_display(self):

        #A symbol table for all symbols
        symbol =   {Permanant_Wall:"#", Brick_Wall:"/",Player: "B",Enemy: "E", 
                    Bomb:"O", Nothing:" ", "explosion":"e"}
        
        #the array to be printed
        to_print = [["" for i in range(self.dimensions[0]*4)] 
                        for j in range(self.dimensions[1]*2)]

        def display_player(i, j):
            to_print[i][j] = '['
            to_print[i][j+1] = '^'
            to_print[i][j+2] = '^'
            to_print[i][j+3] = ']'
            to_print[i+1][j] = ' '
            to_print[i+1][j+1] = ']'
            to_print[i+1][j+2] = '['
            to_print[i+1][j+3] = ' '

        def display_enemy(i, j):
            to_print[i][j] = '['
            to_print[i][j+1] = 'X'
            to_print[i][j+2] = 'X'
            to_print[i][j+3] = ']'
            to_print[i+1][j] = '['
            to_print[i+1][j+1] = '['
            to_print[i+1][j+2] = ']'
            to_print[i+1][j+3] = ']'

        def display_bomb(i, j):
            for row in range(i,i+2):
                for col in range(j,j+4):
                    to_print[row][col] = bomb.display()


        #Filling up the array
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if type(self.board[i][j])==Player:
                    display_player(i*2,j*4)
                    continue;
                elif type(self.board[i][j])==Enemy:
                    display_enemy(i*2,j*4)
                    continue;
                elif type(self.board[i][j])==Bomb:
                    display_bomb(i*2,j*4)
                    continue;
                for small_i in range(i*2,i*2+2):
                    for small_j in range(j*4,j*4+4):
                        to_print[small_i][small_j] = symbol[type(self.board[i][j])] 
        
        #Putting the explosion in the right place if needed
        if Bomb.is_present():
            bomb.display()
            if bomb.exploded():
                for radius in bomb.radius:
                    if (board.is_within_board(radius)):
                        for small_i in range(radius[0]*2,radius[0]*2+2):
                            for small_j in range(radius[1]*4,radius[1]*4+4):
                                to_print[small_i][small_j] = symbol["explosion"]

        
        #Actually printing the board. Phew!
        print(('#'*(self.dimensions[1]*4+4)))
        print(('#'*(self.dimensions[1]*4+4)))
        for i in range(self.dimensions[0]*2):
            print('##',end="")
            for j in range(self.dimensions[1]*4):
                print (to_print[i][j], end = "")
            print('##',end="")
            print()
        print(('#'*(self.dimensions[1]*4+4)))
        print(('#'*(self.dimensions[1]*4+4)))

        #Printing the score and lives:
        print("SCORE:",player.score, "\tNO. OF LIVES:",player.lives)
        

    def update_positions(self):
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                (self.board[i][j]).position = [i, j]

    
