# Example file showing a basic pygame "game loop"
import pygame
from helpers import build_background
from ship import Ship

# pygame setup
pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

# get my background
background = build_background(WIDTH,HEIGHT)

# make a ship 
player1 = Ship(200,200)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            k = pygame.key.name(event.key)
            # check if k is right, left, up down
            if k == 'right':
                player1.theta -= 1
            elif k == 'left':
                player1.theta += 1
            elif k == 'up':
                player1.speed += 1
            elif k == 'down':
                player1.speed -= 1

    # update the ships position
    player1.update()

    # Blit the background to the screen
    screen.blit(background,(0,0))

    # draw the ship
    player1.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()