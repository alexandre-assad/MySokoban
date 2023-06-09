

class Map:
    
    def __init__(self,matrix:list):
        self.matrix = matrix


    def is_movable(self,y,x):
        return self.matrix[y][x].move
    
    
    #We try to know if the actual block is pushable, and the next one is movable to 
    def is_pushable(self,y,x,direction):
        
        if direction == "up":
            
            if self.matrix[y][x-1].value != 3:
                return self.matrix[y][x].push and self.matrix[y][x-1].move
            elif self.matrix[y][x-1].value == 3 and self.matrix[y][x].push==True:
                return "check"
            
        elif direction == "down":
            if self.matrix[y][x+1].value != 3:
                return self.matrix[y][x].push and self.matrix[y][x+1].move
            elif self.matrix[y][x+1].value == 3 and self.matrix[y][x].push==True:
                return "check"
            
        elif direction == "left":
            if self.matrix[y-1][x].value != 3:
                return self.matrix[y][x].push and self.matrix[y-1][x].move
            elif self.matrix[y-1][x].value == 3 and self.matrix[y][x].push==True:
                return "check"

        elif direction == "right":
            if self.matrix[y+1][x].value != 3:
                return self.matrix[y][x].push and self.matrix[y+1][x].move
            elif self.matrix[y+1][x].value == 3 and self.matrix[y][x].push==True:
                return "check"