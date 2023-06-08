

class Player:
    
    def __init__(self,y:int,x:int):
        self.x = x
        self.y = y
        
    def up(self,grille):
        if grille.is_movable(self.y-1,self.x) == True and self.x > 0:
            grille[self.y][self.x] = grille[self.y-1][self.x]
            grille[self.y-1][self.x] = 12
        return grille
    
    def down(self,grille):
        if grille.is_movable(self.y+1,self.x) == True and self.x < len(grille):
            grille[self.y][self.x] = grille[self.y+1][self.x]
            grille[self.y+1][self.x] = 12
        return grille
    
    def left(self,grille):
        if grille.is_movable(self.y,self.x-1) == True and self.y > 0:
            grille[self.y][self.x] = grille[self.y][self.x-1]
            grille[self.y][self.x-1] = 12
        return grille
    
    def right(self,grille):
        if grille.is_movable(self.y,self.x+1) == True and self.y > len(grille[0]):
            grille[self.y][self.x] = grille[self.y][self.x+1]
            grille[self.y][self.x+1] = 12
        return grille
    
    