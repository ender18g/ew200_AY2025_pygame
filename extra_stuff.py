import pygame

def build_background(WIDTH,HEIGHT):
    # make a background surface
    bg = pygame.Surface((WIDTH,HEIGHT))

    # load our water tile
    water = pygame.image.load("assets/Tiles/tile_73.png")

    # get the tile width and height
    tile_w, tile_h = water.get_size()

    # loop over each W, H of the bg surface and blit our water tile
    for x in range(0,WIDTH,tile_w):
        for y in range(0, HEIGHT, tile_h):
            bg.blit(water, (x,y))


    # return the bg
    return bg
