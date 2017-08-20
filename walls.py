
class Brick_Wall(Board_Object):
    def __init__(self):
        super(Brick_Wall, self).__init__()

    def __del__(self):
        board.board[self.position[0]][self.position[1]] = Nothing()

class Permanant_Wall(Board_Object):
    def __init__(self):
        super(Permanant_Wall,self).__init__()