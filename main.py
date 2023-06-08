import pygame
from src.layout.game import *
from src.generator.pygame_event import game_event

def main (state):
    events= pygame.event.get()
    
    if state == "game":
        
        
        display_game(sokoban_map)
        
        for event in events:
            
            sokoban_map = game_event(event,player,sokoban_map)


if "__name__" == "__main__":
    main("game")