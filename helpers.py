import pygame
from random import randint

def build_background(WIDTH,HEIGHT):
    # BUILD THE BACKGROUND WITH TILES
    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((255,0,0))

    # load tile images to variables
    grass = pygame.image.load('assets/Tiles/tile_39.png')     # tile_39
    water = pygame.image.load('assets/Tiles/tile_73.png')     # tile_73
    shoreline = pygame.image.load('assets/Tiles/tile_25.png') # tile_25
    rock = pygame.image.load('assets/Tiles/tile_50.png') # tile_50

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
    
    # add some random rocks
    num_rocks = 3
    # loop over num rocks
    for i in range(num_rocks):
        # generate coords
        coords = (randint(0, WIDTH), randint(0,HEIGHT))
        # blit the rock on the bg
        background.blit(rock, coords)


    # return my bg
    return background

def kill_ships(ship_group, bullet_group, score, num_ships):
        # check for bullets hitting ships
    coll_dict = pygame.sprite.groupcollide(ship_group,bullet_group,0,0)

    # check and see if a bullet collides with something that is not its mother\
    for s,bs in coll_dict.items():
        # ship is k, bullet list is v
        # check for non empty values
        if bs:
            #loop over each bullet check its mom
            for b in bs:
                # check if bullet.mom is the ship
                if b.mom != s:
                    # kill the ship
                    s.kill()
                    # kill the bullet
                    b.kill()
                    score[0] += 1
                    # increase the number of spawned ships by chance
                    if randint(0,10)<3:
                        num_ships[0]+=1

def make_instructions(screen, color):
    # black screen
    screen.fill(color)

    WIDTH = screen.get_width()

    instructions = [
        'Use W, A, S, D to move your ship',
        'Press Spacebar to shoot your cannon',
        'Press P to take a screenshot',
        '',
        '**Press any Key To Play**'
    ]

    # make an instruction font
    i_font = pygame.font.Font('assets/fonts/Kranky-Regular.ttf',size=40)
    spacing = 80
    # render (make surface) for each instruction
    for ii in range(len(instructions)):
        # render the font
        font_surf = i_font.render(instructions[ii], True, light_blue)
        # get a rect
        font_rect = font_surf.get_rect()
        font_rect.center = (WIDTH//2, spacing + ii * spacing)
        # blit it to the screen
        screen.blit(font_surf, font_rect)


def loop_instructions(screen):
    waiting = 1
    running = True
    # if we see the spacebar, exit the loop (break)
    while waiting:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = 0
            if event.type == pygame.KEYDOWN:
                # if any key pressed, break
                waiting = 0
        
        make_instructions(screen,black)

        pygame.display.flip()
    
    return running

from enemy_ship import EnemyShip

def spawn_ships(WIDTH, HEIGHT, num_ships, enemy_group, player1, screen, bullet_group):
    # check the number of ships, and spawn more as needed
    # get the number of ships right now
    n = len(enemy_group)
    for i in range(n, num_ships[0]):
        x = randint(128, WIDTH)
        y = randint(0, HEIGHT)
        speed = randint(1, 5)
        enemy = EnemyShip(player1, screen, x,y, speed,  WIDTH, HEIGHT, bullet_group, color='gray')
        enemy_group.add(enemy)

from datetime import datetime
def take_screenshot(screen):
    print("TAKING SCREENSHOT")
    fn = datetime.now().strftime('%d_%m_%y_%H%M%S.png')
    # take a screenshot
    pygame.image.save(screen, f'screenshots/{fn}')

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


# make some colors
light_blue = pygame.Color('#A2D6F9')
imp_red = pygame.Color('#F8333C')
y_blue = pygame.Color('#355070')
orange = pygame.Color('#FCAB10')
violet = pygame.Color('#6D597A')
black = (0,0,0)