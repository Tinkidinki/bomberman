#from board_object import Board_Object
#from board import Board

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
    
    def move(self, user_input):
        possible_new_position = []

        if user_input == 'a':
            possible_new_position = list(self.position[0]-1,self.position[1])
        elif user_input == 's':
            possible_new_position = list(self.position[0], self.position[1]+1)
        elif user_input == 'd':
            possible_new_position = list(self.position[0]+1,self.position[1])
        elif user_input == 'w':
            possible_new_position = list(self.position[0], self.position[1]-1)
        
        if board.is_within_board(possible_new_position) and board.is_empty(possible_new_position):
            self.position = possible_new_position

    def drop_bomb(self):
        bomb = Bomb(self.position)
    
    def __del__(self):
        e  = Enemy()
        print(Enemy)
        print(e)
        print(Nothing)
        Player.No_of_players -=1
        board.board[self.position[0]][self.position[1]] = Nothing()
