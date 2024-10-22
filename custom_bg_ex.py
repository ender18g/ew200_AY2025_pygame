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
background = pygame.Surface((2*WIDTH,HEIGHT))
dark_green = (47, 153,67)
light_green = (47, 173,67)

# fill the bg with dark_green
background.fill(dark_green)
# make a light_green stripe
stripe_width = 30
stripe = pygame.Surface((stripe_width,HEIGHT))
stripe.fill(light_green)

# blit the the light_green stripe in the x direction
for x in range(0,2*WIDTH,stripe_width*2):
    background.blit(stripe,(x,0))


i=0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit the background to the screen
    screen.blit(background,(i,0))
    i-=3
    if abs(i)>(WIDTH):
        i=0


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()