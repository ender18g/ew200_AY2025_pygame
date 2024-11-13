import pygame
from random import randint

def build_background(WIDTH,HEIGHT):
    # BUILD THE BACKGROUND WITH TILES
    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((255,0,0))

    # load tile images to variables
    grass = pygame.image.load('assets/Tiles/tile_39.png')     # tile_39
    water = pygame.image.load('assets/Tiles/tile_73.png')     # tile_73
    shoreline = pygame.image.load('assets/Tiles/tile_25.png') # tile_25
    rock = pygame.image.load('assets/Tiles/tile_50.png') # tile_50

    # get to the tile_size
    TILE_SIZE = water.get_width()

    # loop over x direction
    for x in range(0,WIDTH,TILE_SIZE):
        # loop over y direction
        for y in range(0,HEIGHT, TILE_SIZE):
            # blit the tile to our BG
            background.blit(water, (x,y))
            if x<TILE_SIZE:
                background.blit(grass, (x,y))
            elif x<(2*TILE_SIZE):
                background.blit(shoreline, (x,y))
    
    # add some random rocks
    num_rocks = 3
    # loop over num rocks
    for i in range(num_rocks):
        # generate coords
        coords = (randint(0, WIDTH), randint(0,HEIGHT))
        # blit the rock on the bg
        background.blit(rock, coords)


    # return my bg
    return background

def kill_ships(ship_group, bullet_group):
        # check for bullets hitting ships
    coll_dict = pygame.sprite.groupcollide(ship_group,bullet_group,0,0)

    # check and see if a bullet collides with something that is not its mother\
    for s,bs in coll_dict.items():
        # ship is k, bullet list is v
        # check for non empty values
        if bs:
            #loop over each bullet check its mom
            for b in bs:
                # check if bullet.mom is the ship
                if b.mom != s:
                    # kill the ship
                    s.kill()
