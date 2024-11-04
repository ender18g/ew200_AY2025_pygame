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
player1 = Ship(500,200, WIDTH, HEIGHT)
enemy1 = Ship(400,400, WIDTH, HEIGHT, color='gray')

# make a sprite group
ship_group = pygame.sprite.Group()

# add our sprite to the sprite group
ship_group.add(player1)
ship_group.add(enemy1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update the ships position
    ship_group.update()

    # check for collision
    has_collided = pygame.sprite.collide_rect(player1,enemy1)
    
    if has_collided:
        player1.kill()

    # Blit the background to the screen
    screen.blit(background,(0,0))

    # draw the ship
    ship_group.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()