
class Brick_Wall(Board_Object):
    walls = []
    def __init__(self):
        super(Brick_Wall, self).__init__()
        Brick_Wall.walls.append(self)

    def die(self):
        board.board[self.position[0]][self.position[1]] = Nothing()
        Brick_Wall.walls.remove(self)

class Permanant_Wall(Board_Object):
    def __init__(self):
        super(Permanant_Wall,self).__init__()