import pygame
from utils.pygame_manager import *
from utils.os_manager import *  

def position_in_grid(y,x):
    pass

def create_display_game():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Space Invader")

def display_game(grid):
    wallImg = pygame.image.load("../../assets/sprites/wall.png").convert_alpha()
    boxImg = pygame.image.load("../../assets/sprites/wall.png").convert_alpha()
    airImg = pygame.image.load("../../assets/sprites/wall.png").convert_alpha()
    playerImg = pygame.image.load("../../assets/sprites/wall.png").convert_alpha()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Space Invader")
    for i in range(len(grid.matrix)):
        for j in range(len(grid.matrix[0])):
            if grid.matrix[i][j] == 0:
                screen.blit(airImg,position_in_grid(i,j))
            elif grid.matrix[i][j] == 1:
                screen.blit(wallImg,position_in_grid(i,j))
            elif grid.matrix[i][j] == 2:
                screen.blit(boxImg,position_in_grid(i,j))
            elif grid.matrix[i][j] == 12:
                screen.blit(playerImg,position_in_grid(i,j))

