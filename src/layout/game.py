import pygame
from src.utils.pygame_manager import *
from src.utils.os_manager import *  


def position_in_grid(y,x):
    return [y*50,x*50]

def create_display_game():
    global wallImg, boxImg, airImg, playerImg,screen
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("My Sokoban")
    wallImg = pygame.image.load(sprite_path("wall.png")).convert_alpha()
    boxImg = pygame.image.load(sprite_path("box.png")).convert_alpha()
    airImg = pygame.image.load(sprite_path("air.png")).convert_alpha()
    playerImg = pygame.image.load(sprite_path("player.png")).convert_alpha()
    
    

def display_game(grid):
    pygame.display.set_caption("My Sokoban")
    for i in range(9):
        for j in range(9):
            if grid.matrix[i][j].value == 0:
                screen.blit(airImg,position_in_grid(i,j))
            elif grid.matrix[i][j].value == 1:
                screen.blit(wallImg,position_in_grid(i,j))
            elif grid.matrix[i][j].value == 2:
                screen.blit(boxImg,position_in_grid(i,j))
            elif grid.matrix[i][j].value == 12:
                screen.blit(playerImg,position_in_grid(i,j))



