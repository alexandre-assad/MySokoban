

class Map:
    
    def __init__(self,matrix:list):
        self.matrix = matrix

    def is_movable(self,y,x):
        if self.matrix[y][x] != 0:
            return False
        else:
            return True