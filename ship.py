from math import cos, sin, pi
import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, WIDTH, HEIGHT, theta=270, color='red'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 0
        self.theta = theta # degrees
        self.color = color
        if color == 'red':
            self.orig_image = pygame.image.load('assets/Ships/ship (3).png')
        else:
            self.orig_image = pygame.image.load('assets/Ships/ship (2).png')
        self.image = self.orig_image # keep orig image to never be rotated
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.screen_w = WIDTH
        self.screen_h = HEIGHT

    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad
    
    def check_keys(self):
        # check keys to move ship around
        keys = pygame.key.get_pressed()
        # check w,s up/down
        if keys[pygame.K_w]:
            self.speed += 0.5
        if keys[pygame.K_s]:
            self.speed -= 0.5
        # check a, d theta left/right
        if keys[pygame.K_a]:
            self.theta += 1
        if keys[pygame.K_d]:
            self.theta -= 1
    
    def check_border(self):
        c_x, c_y = self.rect.center
        # check the border, and set to 0 if we hit the border
        if c_x > self.screen_w or c_x < (0+128*2) or c_y<0 or c_y>self.screen_h:
            self.speed = 0

    def update(self):
        if self.color =='red':   
            self.check_keys() # only red if influenced by keys
          
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta)
        x_dot = cos(theta_rad) * self.speed
        y_dot = sin(theta_rad) * self.speed

        self.x += x_dot
        self.y -= y_dot

        # now rotate the image and drew new rect
        self.image = pygame.transform.rotozoom(self.orig_image, self.theta - 270, 0.7)
        self.rect = self.image.get_rect(center = (self.x, self.y))

        self.check_border()