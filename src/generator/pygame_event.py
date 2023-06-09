import pygame
from src.utils.pygame_manager import *
def game_event(event,player,grid):
    
    if up_key(event):
        player.direction = "up"
        grid = player.movement(grid)
    
    elif down_key(event):
        player.direction = "down"
        grid = player.movement(grid)
        
    elif left_key(event):
        player.direction = "left"
        grid = player.movement(grid)
    
    elif right_key(event):
        player.direction = "right"
        grid = player.movement(grid)

    elif p_key(event):
        grid = player.push(grid)
    
    
    return grid