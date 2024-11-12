# Example file showing a basic pygame "game loop"
import pygame
from helpers import build_background, kill_ships
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

# make a sprite group
ship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# make a ship 
player1 = Ship(screen,500,200, WIDTH, HEIGHT, bullet_group)
enemy1 = Ship(screen, 400,400, WIDTH, HEIGHT, bullet_group, color='gray')

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
    bullet_group.update()

    # check for collision
    has_collided = pygame.sprite.collide_rect(player1,enemy1)

    
    if has_collided:
        player1.kill()

    # Blit the background to the screen
    screen.blit(background,(0,0))

    # draw the ship
    ship_group.draw(screen)
    bullet_group.draw(screen)

    # check for ship collision kill them
    kill_ships(ship_group, bullet_group)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()