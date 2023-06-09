import pygame
from src.layout.game import *
from src.generator.pygame_event import game_event
from src.generator.map import Map
from src.generator.player import Player
from src.generator.block import Block





def main (state):
    events= pygame.event.get()
    
    while state == "game":
        
        
        display_game(sokoban_map)
        
        for event in events:
            if event.type == pygame.QUIT:
                state = "over"
            sokoban_map = game_event(event,player,sokoban_map)


if "__name__" == "__main__":
    main("game")