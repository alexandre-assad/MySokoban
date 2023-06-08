import pygame

def up_key(event):
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_UP:
            return True
        
        return False

def down_key(event):
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_DOWN:
            return True
        
        return False

def left_key(event):
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_LEFT:
            return True
        
        return False
    

def right_key(event):
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_RIGHT:
            return True
        
        return False