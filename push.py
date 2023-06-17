import pygame
from character import *
from character import Character

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

class Push:
    dx = 0

    def __init__(self, x, y, fb, wg):
        self.block = pygame.image.load("img/block.png")
        self.rect = self.block.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.fb = fb
        self.wg = wg
        self.top_collision = False
        self.lock_block = False

    def update(self, block_list, c_type):
        self.lock_block = False
        self.dx = 0
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

        # block and character collision
        self.block_character_collision(c_rect_x, c_dx, c_rect_y, c_img, c_rect, c_momentum, c_dy)

        # pushable with block collision
        self.pushable_block_collision(block_list, c_type, c_rect_x, c_dx, c_rect_y, c_img)


        self.rect.x += self.dx
        screen.blit(self.block, self.rect)

        return self.top_collision

    def block_character_collision(self, c_rect_x, c_dx, c_rect_y, c_img, c_rect, c_momentum, c_dy):
        if self.rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):
            if c_dx < 0:
                self.dx -= 8
            if c_dx > 0:
                self.dx += 8
            Character.fb_dx = 0
            Character.wg_dx = 0

        if self.rect.colliderect(c_rect_x, c_rect_y + c_dy, c_img.get_width(), c_img.get_height()):
            if c_momentum < 0:
                c_rect.top = self.rect.bottom

            elif c_momentum >= 0:  # touch from top
                self.top_collision = True
                c_rect.bottom = self.rect.top - c_dy

    def pushable_block_collision(self, block_list, c_type, c_rect_x, c_dx, c_rect_y, c_img):
        for block in block_list:
            if block.colliderect(self.rect.x + (self.dx + 2), self.rect.y, 34, 34):
                self.dx = 0
                # character with pushable stop collision
                if self.rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):
                    if c_type == "fb":
                        Character.fb_dx = 0
                    if c_type == "wg":
                        Character.wg_dx = 0

                    # self.y_momentum = 0

    def rt_rect(self):
        return self.rect

    def rt_dx(self):
        return self.dx
