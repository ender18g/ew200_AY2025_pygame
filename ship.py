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
        self.shoot_time = 0 # this is to prevent continuous shooting
        self.shoot_wait = 500 # wait ms before next shot
        # load up explosion images
        self.explosion_image = pygame.image.load('assets/Effects/explosion1.png')
        self.explosion_image = pygame.transform.scale_by(self.explosion_image, 6)
        self.explosion_timer = 0
        self.explosion_length = 500

        # load some sounds
        self.shoot_sound = pygame.mixer.Sound('assets/Audio/impactPlank_medium_003.ogg')


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
        # only shoot if the time has elapsed
        if pygame.time.get_ticks() - self.shoot_time > self.shoot_wait:
            # we are allowed to shoot now
            self.shoot_sound.play()
            self.shoot_time = pygame.time.get_ticks()
            # if we have waited long enough, then make bullet
            b = Bullet(self.screen, self, self.x, self.y, self.theta)
            # put the bullet in a group
            self.bullet_group.add(b)
    
    def explode(self):
        # if the timer is already set, do nothing
        if self.explosion_timer ==0:
            # start a timer so that it gets killed later
            self.explosion_timer = pygame.time.get_ticks()
            print("explosion timer set!")
            self.speed = 0

    def track_player(self):
        # This code is in my enemy ship class
        pass

    def update(self):
        if self.color =='red':   
            self.check_keys() # only red if influenced by keys
        else:
            self.track_player()
        
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

        # check on the explosion status
        if self.explosion_timer != 0:
            delta_time = pygame.time.get_ticks() - self.explosion_timer
            # if we have reached kill time, kill the ship
            if delta_time >= self.explosion_length:
                print("killing ship")
                self.kill()
            # ship is in explosion sequence
            # grow the ship based on time
            if delta_time < (self.explosion_length/2):
                # grow the explosion
                self.orig_image = pygame.transform.scale_by(self.explosion_image, delta_time/1000)
            else:
                # shrink the explosion
                self.orig_image = pygame.transform.scale_by(self.explosion_image, self.explosion_length/1000 - (delta_time - self.explosion_length/2)/1000)



