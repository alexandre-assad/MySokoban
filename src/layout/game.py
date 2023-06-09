import pygame
from src.utils.pygame_manager import *
from src.utils.os_manager import *  
from src.generator.game import Game

def position_in_grid(y,x):
    return [y*50,x*50]

def create_display_game():
    global wallImg, boxImg, airImg, playerImg,screen
    pygame.init()
    game_object = Game(screen=pygame.display.set_mode((800,600)),size=[(800,600)])
    pygame.display.set_caption("My Sokoban")
    wallImg = pygame.image.load(sprite_path("wall.png")).convert_alpha()
    boxImg = pygame.image.load(sprite_path("box.png")).convert_alpha()
    airImg = pygame.image.load(sprite_path("air.png")).convert_alpha()
    playerImg = pygame.image.load(sprite_path("player.png")).convert_alpha()
    return game_object
    
    

def display_game(grid,game):
    for i in range(10):
        for j in range(10):
            if grid.matrix[i][j].value == 0:
                game.screen.blit(airImg,position_in_grid(i,j))
            elif grid.matrix[i][j].value == 1:
                game.screen.blit(wallImg,position_in_grid(i,j))
            elif grid.matrix[i][j].value == 2:
                game.screen.blit(boxImg,position_in_grid(i,j))
            elif grid.matrix[i][j].value == 12:
                game.screen.blit(playerImg,position_in_grid(i,j))
    pygame.display.update()



