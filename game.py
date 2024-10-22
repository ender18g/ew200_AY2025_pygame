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
background = pygame.Surface((WIDTH,HEIGHT))
background.fill((50,50,50))

# load tile images to variables


# loop over x direction

# loop over y direction

# blit the tile to our BG








while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background to the screen
    screen.blit(background,(0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()