import pygame

def build_background(WIDTH,HEIGHT):
    # BUILD THE BACKGROUND WITH TILES
    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((255,0,0))

    # load tile images to variables
    grass = pygame.image.load('assets/Tiles/tile_39.png')     # tile_39
    water = pygame.image.load('assets/Tiles/tile_73.png')     # tile_73
    shoreline = pygame.image.load('assets/Tiles/tile_25.png') # tile_25

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

    # return my bg
    return background