import pygame
import math

class Tank():

    def __init__(self, screen):
         """Initialize the tank and set its starting position."""
         self.screen = screen

         # Load the ship image and get its rect.
         self.image = pygame.image.load('images/tank.gif')
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()

         # Start each new ship at the bottom center of the screen.
         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.bottom

         # Movement flag.
         self.moving_right = False
         self.moving_left = False
         self.moving_forward = False
         self.moving_backward = False

         # Anlge of rotaion.
         self.angle = 0

         # Turn on/off rotation blitting. Recent images of rotated tank.
         self.on = 0
         self.recent_image = ''
         self.recent_rect = ''


    def update(self):
        if self.moving_right:
            self.angle -= 2
            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.image, self.angle, 1)
            self.on = 1
            self.recent_image = image
            self.recent_rect =  self.rect
            self.blitme(image, self.rect)

        if self.moving_left:
            self.angle += 2

            # new_image = pygame.transform.rotate(image_clean, self.angle)
            image = pygame.transform.rotozoom(self.image, self.angle, 1)
            self.on = 1
            self.recent_image = image
            self.recent_rect =  self.rect
            self.blitme(image, self.rect)

        if self.moving_forward:
            angle_90 = 1
            speed_factor_y = 2.5 #2.5
            speed_factor_x = 2.8 #3

            if (self.angle > -100 and self.angle < -80) or (self.angle > 260 and self.angle < 280) or (self.angle > -280 and self.angle < -260) or (self.angle > 80 and self.angle < 100) :
                speed_factor_x = 1

            if self.angle > 360 or self.angle < -360:
                if self.angle > 360:
                    self.angle = self.angle - 360
                else:
                    self.angle = self.angle + 360


            if self.angle == 90 or self.angle == -90 or self.angle == 270 or self.angle == -270:
                angle_90 = 0
                if self.angle == 90 or self.angle == -270:
                    difference_between_x_y = -1
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                else:
                    difference_between_x_y = 1
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
            else:
                difference_between_x_y = -1 * math.tan(self.angle * math.pi / 180)

            print(self.angle)



            if self.angle == 0 or self.angle == 360 or self.angle == -360 or self.angle == 180 or self.angle == -180 :
                if self.angle == 0 or self.angle == 360 or self.angle == -360 :
                    self.rect.centery -= speed_factor_y * angle_90
                else:
                    self.rect.centery += speed_factor_y * angle_90
            else:
                print('assignment to rect centerx ', int(speed_factor_x * (difference_between_x_y)))
                # Assigning is for preventing dublicate calling self.angle variable.
                rotation_angle = self.angle

                if (rotation_angle < 0 and rotation_angle > -90) or (rotation_angle < 360 and rotation_angle > 270):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -90 and rotation_angle > -180) or (rotation_angle < 270 and rotation_angle > 180):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx += -1 * int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -180 and rotation_angle > -270) or (rotation_angle < 180 and rotation_angle > 90):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -270 and rotation_angle > -360) or (rotation_angle < 90 and rotation_angle > 0):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))





# _______________________________________________________________________________________________________________________________________
        if self.moving_backward:
            angle_90 = 1
            speed_factor_y = 2.5 #2.5
            speed_factor_x = 2.8 #3

            if (self.angle > -100 and self.angle < -80) or (self.angle > 260 and self.angle < 280) or (self.angle > -280 and self.angle < -260) or (self.angle > 80 and self.angle < 100) :
                speed_factor_x = 1

            if self.angle > 360 or self.angle < -360:
                if self.angle > 360:
                    self.angle = self.angle - 360
                else:
                    self.angle = self.angle + 360


            if self.angle == 90 or self.angle == -90 or self.angle == 270 or self.angle == -270:
                angle_90 = 0
                if self.angle == 90 or self.angle == -270:
                    difference_between_x_y = -1
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                else:
                    difference_between_x_y = 1
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
            else:
                difference_between_x_y = -1 * math.tan(self.angle * math.pi / 180)

            print(self.angle)



            if self.angle == 0 or self.angle == 360 or self.angle == -360 or self.angle == 180 or self.angle == -180 :
                if self.angle == 0 or self.angle == 360 or self.angle == -360 :
                    self.rect.centery += speed_factor_y * angle_90
                else:
                    self.rect.centery -= speed_factor_y * angle_90
            else:
                print('assignment to rect centerx ', int(speed_factor_x * (difference_between_x_y)))
                # Assigning is for preventing dublicate calling self.angle variable.
                rotation_angle = self.angle

                if (rotation_angle < 0 and rotation_angle > -90) or (rotation_angle < 360 and rotation_angle > 270):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx -= int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -90 and rotation_angle > -180) or (rotation_angle < 270 and rotation_angle > 180):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx -= -1 * int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -180 and rotation_angle > -270) or (rotation_angle < 180 and rotation_angle > 90):
                    self.rect.centery -= speed_factor_y * angle_90
                    self.rect.centerx += int(speed_factor_x * (difference_between_x_y))
                elif (rotation_angle < -270 and rotation_angle > -360) or (rotation_angle < 90 and rotation_angle > 0):
                    self.rect.centery += speed_factor_y * angle_90
                    self.rect.centerx += -1 * int(speed_factor_x * (difference_between_x_y))









    def blitme(self, image='', rect=''):
        """Draw the ship at its current location."""
        if self.on == 0:
            # Rotating doesn't start and rotated image is not displayed.
            self.screen.blit(self.image, self.rect)
        else:
            # Rotating start and rotated image is displayed.
            self.on = 1
            self.screen.blit(self.recent_image, self.recent_rect)
            pygame.display.flip()
