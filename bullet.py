import pygame
from math import sin, cos, radians
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen,mom, x,y,theta,speed = 5):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.theta = theta # degrees
        self.image = pygame.image.load('assets\parts\cannonBall.png')
        self.rect = self.image.get_rect()
        # place the bullet
        self.rect.center = (self.x,self.y)
        self.screen = screen
        print(screen)
        self.screen_rect = screen.get_rect()
        self.mom = mom

    
    def update(self):
        dx = self.speed * cos(radians(self.theta))
        dy = self.speed * sin(radians(self.theta))
        
        self.x += dx
        self.y -= dy
        # update the rect
        self.rect.center = (self.x,self.y)

        # check if the bullet is inside the screen
        if not self.screen_rect.contains(self.rect):
            # remove the bullet
            self.kill()




