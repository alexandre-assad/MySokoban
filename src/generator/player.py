
class Player:
    
    def __init__(self,y:int,x:int,direction=""):
        self.x = x
        self.y = y
        self.direction = direction
        
    def movement(self,grid):
        if self.direction == "up":
            
            if grid.is_movable(self.y-1,self.x) == True and self.x > 0:
                
                grid[self.y][self.x] = grid[self.y-1][self.x]
                grid[self.y-1][self.x] = 12
                
            return grid
        
        elif self.direction == "down":
            
            if grid.is_movable(self.y+1,self.x) == True and self.x < len(grid):
                
                grid[self.y][self.x] = grid[self.y+1][self.x]
                grid[self.y+1][self.x] = 12
                
            return grid
        
        elif self.direction == "left":
            
            if grid.is_movable(self.y,self.x-1) == True and self.y > 0:
                
                grid[self.y][self.x] = grid[self.y][self.x-1]
                grid[self.y][self.x-1] = 12
                
            return grid
            
        elif self.direction == "right":
            
            if grid.is_movable(self.y,self.x+1) == True and self.y > len(grid[0]):
                
                grid[self.y][self.x] = grid[self.y][self.x+1]
                grid[self.y][self.x+1] = 12
                
            return grid

        else:
            print("erreur")
            return grid
        
    

    def push(self,grid):
        
        if self.direction == "up":
            
            if grid[self.y-1][self.x].is_pushable == True:
                pass
        
        pass
    
    
    