import random
import builtins

def generate_board(dimensions,enemies_left,brick_walls_left):
    board = [[Nothing() for i in range(dimensions[1])] for j in range(dimensions[0])]
    builtins.player = Player()
    choices = []
    no_of_permanant_walls = 0

    for i in range(enemies_left):
        choices.append('E')
    
    for i in range(brick_walls_left):
        choices.append('B')
    
    if (dimensions[0]%2==0):
        no_of_permanant_walls = (dimensions[0]//2)**2
    else:
        no_of_permanant_walls = ((dimensions[0]-1)//2)**2

    for i in range(dimensions[0]*dimensions[1] - (enemies_left + brick_walls_left + no_of_permanant_walls + 1 )):
        choices.append('N')

    for row in range(dimensions[0]):
        for col in range(dimensions[1]):
            
            #print("current iteration","[",row,",",col,"]")

            if (row==0 and col==0):
                board[row][col] = player
                continue;

            if (row %2 != 0 and col %2 !=0):
                board[row][col] = Permanant_Wall()
                continue
            
            else:
                ob = random.choice(choices)

                if (ob == 'E'):
                    board[row][col] = Enemy()
                    enemies_left-=1
                    
                elif (ob == 'B'):
                    board[row][col] = Brick_Wall()
                    brick_walls_left-=1
                
                else:
                    board[row][col] = Nothing()
                
                choices.remove(ob)

    return board
                    
                    
            