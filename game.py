# Example file showing a basic pygame "game loop"
import pygame
from helpers import build_background, kill_ships
from ship import Ship

# make some colors
light_blue = pygame.Color('#A2D6F9')
imp_red = pygame.Color('#F8333C')
y_blue = pygame.Color('#355070')
orange = pygame.Color('#FCAB10')
violet = pygame.Color('#6D597A')

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

# make font
title_font = pygame.font.Font('assets/fonts/Kranky-Regular.ttf',size=80)

# render a font
title_text = "Life's A Beach"
title_color = (0,0,255)
title_surface = title_font.render(title_text,1,imp_red )
title_rect = title_surface.get_rect()
title_rect.center = (WIDTH//2, HEIGHT//2)
bg_alpha = 0
show_title = 1 # boolean to say if title should be blit


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

     # make the bg a bit darker
    background.set_alpha(bg_alpha)
    title_surface.set_alpha(255-0.4*bg_alpha)
    bg_alpha +=1


    # Blit the background to the screen
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    # draw text
    screen.blit(title_surface, title_rect)

    # draw the ship
    ship_group.draw(screen)
    bullet_group.draw(screen)

    # check for ship collision kill them
    kill_ships(ship_group, bullet_group)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()