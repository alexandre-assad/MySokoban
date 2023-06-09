import pygame
from src.layout.game import *
from src.generator.pygame_event import *
from src.generator.map import Map
from src.generator.player import Player
from src.generator.block import Block


def generate_map(Player):
    wallBlock = Block(1)
    airBlock = Block(0,False,True)
    
    line = [wallBlock for _ in range(10)]
    maps = [line]
    
    for i in range(8):
        
        new_list = [wallBlock]
        
        for j in range(8):
            
            if i == Player.y-1 and j== Player.x-1:
                new_list.append(Player)
                
            else:
                
                new_list.append(airBlock)
                
        new_list.append(wallBlock)
        maps.append(new_list)
        
    maps.append([wallBlock for _ in range(10)])
    
    return maps

first_player = Player(3,6,"")
sokoban_map = Map(generate_map(first_player))

sokoban_map.matrix[4][4] = Block(2,True,False)
sokoban_map.matrix[5][5] = Block(2,True,False)
sokoban_map.matrix[7][3] = Block(3,False,False)
sokoban_map.matrix[2][7] = Block(3,False,False)

def main (state,sokoban_map,first_player):
    game_object = create_display_game()
    while state == "game":
        events = pygame.event.get()
        state = display_game(sokoban_map,game_object,first_player)
        for event in events:
            if event.type == pygame.QUIT:
                state = "over"
                
            sokoban_map = game_event(event,first_player,sokoban_map)

    pygame.quit()
    
if __name__ == "__main__":
    main("game",sokoban_map,first_player)