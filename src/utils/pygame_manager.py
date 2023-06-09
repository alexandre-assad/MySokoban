import pygame


# for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#     #Keyboard
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_LEFT:


"""
If a movement key is pressed,
We do player.direction = key_direction
We do player.movement(grid)

If a push key is press,
We do player.push(grid)
"""


def up_key(event):

    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_UP:
            print("ho")
            return True
        print("ha")
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

def r_key(event):
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_r:
            return True
        
        return False