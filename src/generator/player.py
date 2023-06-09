

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
            
            if grid.is_movable(self.y,self.x-1) and self.x > 0:
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y][self.x-1]
                grid.matrix[self.y][self.x-1] = self
                self.x -=1
                
            return grid
        
        elif self.direction == "down":
            
            if grid.is_movable(self.y,self.x+1) and self.x < len(grid.matrix):
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y][self.x+1]
                grid.matrix[self.y][self.x+1] = self
                self.x +=1
                
            return grid
        
        elif self.direction == "left":
            
            if grid.is_movable(self.y-1,self.x) and self.y > 0:
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y-1][self.x] = self
                self.y -= 1
                
            return grid
            
        elif self.direction == "right":
            
            if grid.is_movable(self.y+1,self.x) and self.y < len(grid.matrix[0]):
                
                grid.matrix[self.y][self.x] = grid.matrix[self.y+1][self.x]
                grid.matrix[self.y+1][self.x] = self
                self.y += 1

            return grid

        else:
            print("erreur")
            return grid
        
    

    def push(self,grid):
        
        if self.direction == "up":
            
            if grid.is_pushable(self.y,self.x-1,self.direction) == "check":
                
                grid.matrix[self.y][self.x-2].value = 2
                grid.matrix[self.y][self.x-2].push = False
                grid.matrix[self.y][self.x-2].move = False
                grid.matrix[self.y][self.x-1].value =0
                grid.matrix[self.y][self.x-1].push =False
                grid.matrix[self.y][self.x-1].move =True 
            
            elif grid.is_pushable(self.y,self.x-1,self.direction) :
                
                old_block = grid.matrix[self.y][self.x-2]
                grid.matrix[self.y][self.x-2] = grid.matrix[self.y][self.x-1]
                grid.matrix[self.y][self.x-1] = old_block
        
        elif self.direction == "down":
            try:
                if grid.is_pushable(self.y,self.x+1,self.direction) == "check":
                    
                    grid.matrix[self.y][self.x+2].value = 2
                    grid.matrix[self.y][self.x+2].push = False
                    grid.matrix[self.y][self.x+2].move = False
                    grid.matrix[self.y][self.x+1].value =0
                    grid.matrix[self.y][self.x+1].push =False
                    grid.matrix[self.y][self.x+1].move =True 
                    
                elif grid.is_pushable(self.y,self.x+1,self.direction) :
                    
                    old_block = grid.matrix[self.y][self.x+2]
                    grid.matrix[self.y][self.x+2] = grid.matrix[self.y][self.x+1]
                    grid.matrix[self.y][self.x+1] = old_block
            except:
                pass
        elif self.direction == "right":
            try:
                if grid.is_pushable(self.y+1,self.x,self.direction) == "check":
                    
                    grid.matrix[self.y+2][self.x].value = 2
                    grid.matrix[self.y+2][self.x].push = False
                    grid.matrix[self.y+2][self.x].move = False
                    grid.matrix[self.y+1][self.x].value =0
                    grid.matrix[self.y+1][self.x].push =False
                    grid.matrix[self.y+1][self.x].move =True 
                    
                elif grid.is_pushable(self.y+1,self.x,self.direction):
                    
                    old_block = grid.matrix[self.y+2][self.x]
                    grid.matrix[self.y+2][self.x] = grid.matrix[self.y+1][self.x]
                    grid.matrix[self.y+1][self.x] = old_block
            except:
                pass
        
        elif self.direction == "left":
            
            if grid.is_pushable(self.y-1,self.x,self.direction) == "check":
                
                grid.matrix[self.y-2][self.x].value =2
                grid.matrix[self.y-2][self.x].push = False
                grid.matrix[self.y-2][self.x].move = False
                grid.matrix[self.y-1][self.x].value =0
                grid.matrix[self.y-1][self.x].push =False
                grid.matrix[self.y-1][self.x].move =True
                
            elif grid.is_pushable(self.y-1,self.x,self.direction):
                
                old_block = grid.matrix[self.y-2][self.x]
                grid.matrix[self.y-2][self.x] = grid.matrix[self.y-1][self.x]
                grid.matrix[self.y-1][self.x] = old_block
                
            
        return grid
    
    
    