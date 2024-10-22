# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

# BUILD THE BACKGROUND WITH TILES
background = pygame.Surface((WIDTH*2,HEIGHT))
background.fill((255,0,0))

# load tile images to variables
grass = pygame.image.load('assets/Tiles/tile_39.png')     # tile_39
water = pygame.image.load('assets/Tiles/tile_73.png')     # tile_73
shoreline = pygame.image.load('assets/Tiles/tile_25.png') # tile_25

# get to the tile_size
TILE_SIZE = water.get_width()

# loop over x direction
for x in range(0,WIDTH*2,TILE_SIZE):
    # loop over y direction
    for y in range(0,HEIGHT, TILE_SIZE):
        # blit the tile to our BG
        background.blit(water, (x,y))
        if x<TILE_SIZE:
            background.blit(grass, (x,y))
        elif x<(2*TILE_SIZE):
            background.blit(shoreline, (x,y))

i = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background to the screen
    screen.blit(background,(i,0))

    i-=1

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()