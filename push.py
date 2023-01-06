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
        self.img_rect = self.block.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y

        self.fb = fb
        self.wg = wg
        self.top_collision = False

    def update(self, block_list, c_type):
        lock_block = False
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

        if self.img_rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):
            # Character.dx = 0
            if not lock_block:
                if c_dx < 0:
                    self.dx -= 8
                if c_dx > 0:
                    self.dx += 8
            # if c_type == "fb" and \
            #         self.img_rect.colliderect((self.wg.rt_rect().x + Character.wg_dx, self.wg.rt_rect().y, self.wg.rt_img().get_width(), self.wg.rt_img().get_height())):
            #     Character.fb_dx = 0
            #     Character.wg_dx = 0
            #     self.dx = 0
            #     # print(self.dx)
            # if c_type == "wg" and \
            #         self.img_rect.colliderect((self.fb.rt_rect().x + Character.fb_dx, self.fb.rt_rect().y,
            #                                    self.fb.rt_img().get_width(), self.fb.rt_img().get_height())):
            #     Character.fb_dx = 0
            #     Character.wg_dx = 0
            #     self.dx = 0
            #     # print(self.dx)

        if self.img_rect.colliderect(c_rect_x, c_rect_y + c_dy, c_img.get_width(), c_img.get_height()):
            if c_momentum < 0:
                c_rect.top = self.img_rect.bottom

            elif c_momentum >= 0:  # touch from top
                self.top_collision = True
                c_rect.bottom = self.img_rect.top - c_dy

        # pushable with block collision
        for block in block_list:
            if block.colliderect(self.img_rect.x + (self.dx + 2), self.img_rect.y, 34, 34):
                self.dx = 0
                # character with pushable stop collision
                if self.img_rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):
                    if c_type == "fb":
                        Character.fb_dx = 0
                        print("fb collided")
                    if c_type == "wg":
                        Character.wg_dx = 0
                        print("wg collided")
        if self.img_rect.colliderect((c_rect_x + c_dx, c_rect_y, c_img.get_width(), c_img.get_height())):

            if c_type == "fb" and \
                    self.img_rect.colliderect((self.wg.rt_rect().x + Character.wg_dx, self.wg.rt_rect().y, self.wg.rt_img().get_width(), self.wg.rt_img().get_height())):
                Character.fb_dx = 0
                Character.wg_dx = 0
                self.dx = 0
                # print(self.dx)
            if c_type == "wg" and \
                    self.img_rect.colliderect((self.fb.rt_rect().x + Character.fb_dx, self.fb.rt_rect().y,
                                               self.fb.rt_img().get_width(), self.fb.rt_img().get_height())):
                Character.fb_dx = 0
                Character.wg_dx = 0
                self.dx -= 100
                print(self.dx)

        self.img_rect.x += self.dx
        screen.blit(self.block, self.img_rect)

        return self.top_collision

    def rt_rect(self):
        return self.img_rect

    def rt_dx(self):
        return self.dx
