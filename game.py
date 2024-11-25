# Example file showing a basic pygame "game loop"
import pygame
from helpers import build_background, kill_ships, make_instructions, loop_instructions
from ship import Ship
from enemy_ship import EnemyShip
from random import randint
from helpers import y_blue, light_blue, imp_red, orange, violet, black
from helpers import spawn_ships, take_screenshot, check_ship_collide

# pygame setup
pygame.init()
pygame.mixer.init()

# load background music
bg_music = pygame.mixer.Sound('assets/mp3/info_flow.mp3')
bg_music.set_volume(0.5)
bg_music.play(-1)


WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

# get my background
background = build_background(WIDTH,HEIGHT)

# make a sprite group
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_ships_group = pygame.sprite.Group()

# make a ship 
player1 = Ship(screen,500,200,0, WIDTH, HEIGHT, bullet_group)
player_group.add(player1)  

num_ships = [1]

spawn_ships(WIDTH, HEIGHT, num_ships, enemy_group, player1, screen, bullet_group)

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

# make a score
score = [0]
score_font = pygame.font.Font('assets/fonts/Kranky-Regular.ttf',size=55)


# Loop the instruction screen
running = loop_instructions(screen)

### MAIN GAME LOOP  ##################################
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                take_screenshot(screen)

    spawn_ships(WIDTH, HEIGHT, num_ships, enemy_group, player1, screen, bullet_group)
    all_ships_group.add(player_group)
    all_ships_group.add(enemy_group)

    # update the ships position
    enemy_group.update()
    player_group.update()
    bullet_group.update()


    # check for collision
    check_ship_collide(player1,num_ships, score, all_ships_group)

     # make the bg a bit darker
    #background.set_alpha(bg_alpha)
    
    title_surface.set_alpha(255 * 2 - bg_alpha)
    bg_alpha +=1

    # Blit the background to the screen
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    # check for rock explosions
    [ship.check_rocks() for ship in all_ships_group]


    # draw text
    screen.blit(title_surface, title_rect)
    score_text = f"Score: {score[0]}"
    score_surface = score_font.render(score_text,1, violet)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (0,0)
    screen.blit(score_surface, score_rect)

    # draw the ship
    enemy_group.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)

    # check for ship collision kill them
    kill_ships(enemy_group, bullet_group, score,  num_ships)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()