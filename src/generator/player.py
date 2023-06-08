
class Player:
    
    def __init__(self,y:int,x:int):
        self.x = x
        self.y = y
        
    def movement(self,grille,direction:str):
        if direction == "up":
            
            if grille.is_movable(self.y-1,self.x) == True and self.x > 0:
                
                grille[self.y][self.x] = grille[self.y-1][self.x]
                grille[self.y-1][self.x] = 12
                
            return grille
        
        elif direction == "down":
            
            if grille.is_movable(self.y+1,self.x) == True and self.x < len(grille):
                
                grille[self.y][self.x] = grille[self.y+1][self.x]
                grille[self.y+1][self.x] = 12
                
            return grille
        
        elif direction == "left":
            
            if grille.is_movable(self.y,self.x-1) == True and self.y > 0:
                
                grille[self.y][self.x] = grille[self.y][self.x-1]
                grille[self.y][self.x-1] = 12
                
            return grille
            
        elif direction == "right":
            
            if grille.is_movable(self.y,self.x+1) == True and self.y > len(grille[0]):
                
                grille[self.y][self.x] = grille[self.y][self.x+1]
                grille[self.y][self.x+1] = 12
                
            return grille

        else:
            print("erreur")
            return grille
    
    
    