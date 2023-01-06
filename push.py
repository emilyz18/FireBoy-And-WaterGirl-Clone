import pygame
from character import *
from character import Character

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))


class Push:
    def __init__(self, x, y, fb, wg):
        self.block = pygame.image.load("img/block.png")
        self.img_rect = self.block.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y

        self.fb = fb
        self.wg = wg

    def update(self):
        dx = 0
        # dy = 0
        wg_rect = self.wg.rt_rect()
        wg_img = self.wg.rt_img()
        wg_momentum = self.wg.rt_momentum()
        top_collision = False

        if self.img_rect.colliderect((wg_rect.x + Character.dx, wg_rect.y, wg_img.get_width(), wg_img.get_height())):
            # Character.dx = 0
            if Character.dx < 0:
                dx -= 8
            if Character.dx > 0:
                dx += 8

        if self.img_rect.colliderect(wg_rect.x, wg_rect.y + Character.dy, wg_img.get_width(), wg_img.get_height()):
            if wg_momentum < 0:
                wg_rect.top = self.img_rect.bottom

                # Character.dy = self.img_rect.bottom - wg_rect.top

            elif wg_momentum >= 0:  # touch from top
                top_collision = True
                wg_rect.bottom = self.img_rect.top - Character.dy
                # Character.dy = self.img_rect.top - wg_rect.bottom

        self.img_rect.x += dx
        screen.blit(self.block, self.img_rect)

        return top_collision
