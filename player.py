#from board_object import Board_Object
#from board import Board
from nothing import Nothing
import builtins

class Player(Board_Object):
    
    No_of_players = 0

    @staticmethod
    def all_dead():
        if Player.No_of_players == 0:
            return True
        else:
            return False
    
    def __init__(self):
        Player.No_of_players+=1
        super(Player,self).__init__()
        self.lives = 10 #Obviously bad coding style, I'll put this in a variable later
        self.score = 0
    
    def move(self, user_input):
        possible_new_position = []

        if user_input == 'a':
            possible_new_position = [self.position[0],self.position[1]-1]
        elif user_input == 's':
            possible_new_position = [self.position[0]+1, self.position[1]]
        elif user_input == 'd':
            possible_new_position = [self.position[0],self.position[1]+1]
        elif user_input == 'w':
            possible_new_position = [self.position[0]-1, self.position[1]]
        
        #print(possible_new_position)
        #print(board.is_within_board(possible_new_position),"is within board")
        #print(board.is_empty(possible_new_position), "is empty")
        if board.is_within_board(possible_new_position) and board.is_empty(possible_new_position):
            if board.board[self.position[0]][self.position[1]] == self: 
                board.board[self.position[0]][self.position[1]] = Nothing()
            self.position = possible_new_position
            board.board[self.position[0]][self.position[1]] = self

    def drop_bomb(self):
        builtins.bomb = Bomb(self.position)
        #print ("IN THE DROB BOMB METHOD - BOMB POSITION",self.position)
    
    def die(self):
        # e  = Enemy()
        # print(Enemy)
        # print(e)
        # print(Nothing)
        if self.lives == 0:
            Player.No_of_players -=1
            board.board[self.position[0]][self.position[1]] = Nothing()
        else:
            self.lives -=1
        
            
        
