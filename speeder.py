import pygame
from character import *

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
class Speeder:
    def __init__(self, x, y, fb, wg):
        self.speeder = pygame.image.load("img/speeder.png")
        self.speeder = pygame.transform.scale(self.speeder, (68 * 2, 18))
        self.img_rect = self.speeder.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y + 10

        self.img_left = pygame.transform.flip(self.speeder, True, False)
        self.img_rect_left = self.img_left.get_rect()
        self.img_rect_left.x = x
        self.img_rect_left.y = y + 10

        self.fb = fb
        self.wg = wg
        self.top_collision = False

    def draw(self):
        screen.blit(self.speeder, self.img_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.img_rect, 2)


    def turn_on(self, c_type):
        self.top_collision = False

        if c_type == "fb":
            c_rect = self.fb.rt_rect()
            c_img = self.fb.rt_img()
            c_momentum = self.fb.rt_momentum()

            c_rect_x = c_rect.x
            c_dx = Character.fb_dx
            c_dy = Character.fb_dy
            c_rect_y = c_rect.y
        if c_type == "wg":
            c_rect = self.wg.rt_rect()
            c_img = self.wg.rt_img()
            c_momentum = self.wg.rt_momentum()

            c_rect_x = c_rect.x
            c_dx = Character.wg_dx
            c_dy = Character.wg_dy
            c_rect_y = c_rect.y

        if self.img_rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):
            if c_type == "fb":
                Character.fb_dx = 0
            if c_type == "wg":
                Character.wg_dx = 0

        if self.img_rect.colliderect(c_rect_x, c_rect_y + c_dy, c_img.get_width(), c_img.get_height()):
            if c_momentum < 0:

                c_rect.top = self.img_rect.bottom

            elif c_momentum >= 0:  # touch from top
                self.top_collision = True
                c_rect.bottom = self.img_rect.top - c_dy
                if c_type == "fb":
                        Character.fb_dx += 2
                if c_type == "wg":
                        Character.wg_dx += 2


        return self.top_collision




