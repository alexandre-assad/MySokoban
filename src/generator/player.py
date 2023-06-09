

class Player:
    
    def __init__(self,y:int,x:int,direction=""):
        self.x = x
        self.y = y
        self.direction = direction
        self.value = 12
        
    def __repr__(self):
        return str(self.value)
        
    def movement(self,grid):
        
        if self.direction == "up":
            
            if grid.is_movable(self.y-1,self.x) and self.x > 0:
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y-1][self.x] = 12
                self.y -=1
                
            return grid
        
        elif self.direction == "down":
            
            if grid.is_movable(self.y+1,self.x) and self.x < len(grid):
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y+1][self.x]
                grid.matrix[self.y+1][self.x] = 12
                self.y += 1
                
            return grid
        
        elif self.direction == "left":
            
            if grid.is_movable(self.y,self.x-1) and self.y > 0:
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y][self.x-1]
                grid.matrix[self.y][self.x-1] = 12
                self.x -= 1
                
            return grid
            
        elif self.direction == "right":
            
            if grid.is_movable(self.y,self.x+1) and self.y > len(grid[0]):
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y][self.x+1]
                grid.matrix[self.y][self.x+1] = 12
                self.x +=1
                
            return grid

        else:
            print("erreur")
            return grid
        
    

    def push(self,grid):
        
        if self.direction == "up":
            
            if grid.is_pushable(self.y-1,self.x,self.direction):
                
                old_block = grid.matrix[self.y-2][self.x]
                grid.matrix[self.y-2][self.x] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y-1][self.x] = old_block
        
        elif self.direction == "up":
            
            if grid.is_pushable(self.y+1,self.x,self.direction):
                
                old_block = grid.matrix[self.y+2][self.x]
                grid.matrix[self.y+2][self.x] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y+1][self.x] = old_block
                
        elif self.direction == "right":
            
            if grid.is_pushable(self.y,self.x+1,self.direction):
                
                old_block = grid.matrix[self.y][self.x+2]
                grid.matrix[self.y][self.x+2] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y][self.x+1] = old_block
        
        elif self.direction == "left":
            
            if grid.is_pushable(self.y,self.x-1,self.direction):
                
                old_block = grid.matrix[self.y][self.x-2]
                grid.matrix[self.y][self.x-2] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y][self.x-1] = old_block
    
    
    