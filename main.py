import pygame
from utils.pygame_manager.py import *

def main (state):
    
    if state == "game":
        
        
        display_game()
        
        for event in pygame.event.get():
            
            game_event(event)


if "__name__" == "__main__":
    main("game")