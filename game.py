# Example file showing a basic pygame "game loop"
import pygame
from helpers import build_background, kill_ships
from ship import Ship
from enemy_ship import EnemyShip
from random import randint

# make some colors
light_blue = pygame.Color('#A2D6F9')
imp_red = pygame.Color('#F8333C')
y_blue = pygame.Color('#355070')
orange = pygame.Color('#FCAB10')
violet = pygame.Color('#6D597A')

# pygame setup
pygame.init()
pygame.mixer.init()

# load background music
bg_music = pygame.mixer.Sound('assets/Steel_jingles/jingles_STEEL01.ogg')
#bg_music.play(-1)




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


def spawn_ships(WIDTH, HEIGHT, num_ships, enemy_group):
    # check the number of ships, and spawn more as needed
    # get the number of ships right now
    n = len(enemy_group)
    for i in range(n, num_ships[0]):
        x = randint(128, WIDTH)
        y = randint(0, HEIGHT)
        speed = randint(1, 5)
        enemy = EnemyShip(player1, screen, x,y, speed,  WIDTH, HEIGHT, bullet_group, color='gray')
        enemy_group.add(enemy)

def check_ship_collide(player1, num_ships, score, all_ships_group):
    # loop over ALL ships and check for collision
    for si in all_ships_group:
        for sj in all_ships_group:
            if si==sj:
                continue
            if pygame.sprite.collide_mask(si,sj):
                if player1 != si:
                    si.explode()
                if player1 != sj:
                    sj.explode()       

# add our sprite to the sprite group

num_ships = [1]

spawn_ships(WIDTH, HEIGHT, num_ships, enemy_group)

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

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    spawn_ships(WIDTH, HEIGHT, num_ships, enemy_group)
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

    # get the color at an xy position on the screen
    r,g,b,_ = screen.get_at(player1.rect.center)
    
    # check the r g and b to see if we are on water
    if r in range(170,181) and g in range(220,241) and b in range(240,256):
        pass
    else:
        player1.explode()


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