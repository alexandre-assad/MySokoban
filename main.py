import pygame
from src.layout.game import *
from src.generator.pygame_event import *
from src.generator.map import Map
from src.generator.player import Player
from src.generator.block import Block


def generate_map(Player):
    wallBlock = Block(1)
    airBlock = Block(0,False,True)
    boxBlock = Block(2,True,False)
    line = [wallBlock for i in range(10)]
    maps = [line]
    for i in range(8):
        new_list = [wallBlock]
        for j in range(8):
            if i == Player.y and j== Player.x:
                new_list.append(Player)
            else:
                new_list.append(airBlock)
        new_list.append(wallBlock)
        maps.append(new_list)
    maps.append([wallBlock for i in range(10)])
    return maps

first_player = Player(3,6,"up")
sokoban_map = Map(generate_map(first_player))


def main (state,sokoban_map,first_player):
    create_display_game()
    events= pygame.event.get()
    while state == "game":
        display_game(sokoban_map)
        
        for event in events:
            if event.type == pygame.QUIT:
                state = "over"
            sokoban_map = game_event(event,first_player,sokoban_map)


if __name__ == "__main__":
    main("game",sokoban_map,first_player)