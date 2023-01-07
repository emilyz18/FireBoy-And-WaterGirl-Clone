import pygame.image
from character import *

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))


class Tramp:
    def __init__(self, x, y, fb, wg):
        self.vent = pygame.image.load("img/tramp.png")
        self.vent = pygame.transform.scale(self.vent, (68, 24))
        self.img_rect = self.vent.get_rect()

        self.img_rect.x = x
        self.img_rect.y = y + 10
        self.fb = fb
        self.wg = wg
        self.top_collision = False

    def draw(self):
        screen.blit(self.vent, self.img_rect)
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
                    Character.fb_dy -= 300

                if c_type == "wg":
                    Character.wg_dy -= 300

        return self.top_collision
