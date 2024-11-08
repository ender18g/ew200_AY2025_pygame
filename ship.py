from math import cos, sin, pi, radians
import pygame
from bullet import Bullet

class Ship(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=270, color='red'):
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
        self.length = self.rect.height + 5
        self.rect.center = (self.x, self.y)
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.max_speed = 5
        self.reverse_time = pygame.time.get_ticks()
        self.bullet_group = bullet_group
        self.screen = screen


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
        
        # check for space bar to shoot
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def check_border(self):
        # make sure our ship rect is inside of some rect we set
        border_rect = pygame.rect.Rect(0,0,self.screen_w, self.screen_h)
        #if the ships rectangle leaves border, then set speed to 0
        if not border_rect.contains(self.rect):
            # only reverse if its been >500ms from last time
            if pygame.time.get_ticks() - self.reverse_time > 500:
                self.speed = -0.2 *self.speed
                #self.theta -=90
                # rese the timer
                self.reverse_time = pygame.time.get_ticks()
 
    def shoot(self):

        # make a bullet instance
        b = Bullet(self.screen, self, self.x, self.y, self.theta)
        # put the bullet in a group
        self.bullet_group.add(b)


    def update(self):
        if self.color =='red':   
            self.check_keys() # only red if influenced by keys
        
        # check and make sure we are moving too fast
        if self.speed > self.max_speed:
            self.speed = self.max_speed 
        elif self.speed < -self.max_speed:
            self.speed = -self.max_speed
          
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