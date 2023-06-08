
class Map:
    
    def __init__(self,matrix:list):
        self.matrix = matrix

    
    def is_movable(self,y,x):
        return self.matrix[y][x].move
    
    
    #We try to know if the actual block is pushable, and the next one is movable to 
    def is_pushable(self,y,x,direction):
        
        if self.direction == "up":
            
            if self.matrix[y][x].push == True and self.matrix[y-1][x].move == True:
                
                return True
            
            else:
                
                return False
            
        elif self.direction == "down":
            
            if self.matrix[y][x].push == True and self.matrix[y+1][x].move == True:
                
                return True
            
            else:
                
                return False
            
        elif self.direction == "left":
            
            if self.matrix[y][x].push == True and self.matrix[y][x-1].move == True:
                
                return True
            
            else:
                
                return False
        
        elif self.direction == "up":
            
            if self.matrix[y][x].push == True and self.matrix[y][x+1].move == True:
                
                return True
            
            else:
                
                return False