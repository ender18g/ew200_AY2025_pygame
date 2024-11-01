from math import cos, sin, pi
import pygame

class Ship():
    def __init__(self, x, y, WIDTH, HEIGHT, theta=270, color='red'):
        self.x = x
        self.y = y
        self.speed = 0
        self.theta = theta # degrees
        self.image = pygame.image.load('assets/Ships/ship (3).png')
        self.rect = self.image.get_rect()
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
        self.check_keys()   
        # get x and y components of speed
        theta_rad = self.deg_to_rad(self.theta)
        x_dot = cos(theta_rad) * self.speed
        y_dot = sin(theta_rad) * self.speed

        self.x += x_dot
        self.y -= y_dot

        self.check_border()

    
    def draw(self, screen):
        # rotate our image
        new_image = pygame.transform.rotozoom(self.image, self.theta - 270, 0.7)
        # update the rectangle W,H
        self.rect = new_image.get_rect()
        # update our rectangle X,Y
        self.rect.center = (self.x, self.y)
        print(self.rect)

        screen.blit(new_image, self.rect.center)
