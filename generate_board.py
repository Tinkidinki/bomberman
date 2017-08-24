import random

def generate_board(dimensions,enemies_left,brick_walls_left):
    board = [[Nothing() for i in range(dimensions[1])] for j in range(dimensions[0])]
    choices = ['N','B','E','N','N','N']

    for row in range(dimensions[0]):
        for col in range(dimensions[1]):
            if (row %2 != 0 and col %2 !=0):
                board[row][col] = Permanant_Wall()
                continue
            
            else:
                ob = random.choice(choices)

                if (ob == 'E'):
                    board[row][col] = Enemy()
                    enemies_left-=1

                    if (enemies_left == 0):
                        choices.remove('E')
                    
                elif (ob == 'B'):
                    board[row][col] = Brick_Wall()
                    brick_walls_left-=1

                    if (brick_walls_left == 0):
                        choices.remove('B')
                
                else:
                    board[row][col] = Nothing()
            
    board[0][0] = player

    return board
                    
                    
            