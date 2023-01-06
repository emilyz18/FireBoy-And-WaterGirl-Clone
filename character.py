import pygame

import game
from control import *
from game import *


# from world import World


class Character:
    dx = 0
    dy = 0

    def __init__(self, x, y):
        # self.block = pygame.image.load("img/block.png")
        # self.img_rect = self.block.get_rect()
        # self.img_rect.x = x
        # self.img_rect.y = y

        self.y_momentum = 0

        self.air_timer = 0

    # def draw(self):
    # game.screen.blit(self.fb, self.rect)
    # game.screen.blit(self.wg, self.rect)

    def move(self, type, blocks_list, push):
        Character.dx = 0
        Character.dy = 0
        key = pygame.key.get_pressed()
        if type == "fb":
            controls = [key[pygame.K_LEFT], key[pygame.K_RIGHT], key[pygame.K_UP]]
        if type == "wg":
            controls = [key[pygame.K_a], key[pygame.K_d], key[pygame.K_w]]

        if controls[0]:  # left
            Character.dx -= 8
        if controls[1]:  # right
            Character.dx += 8
        if controls[2]:  # jump
            if self.air_timer < 5:
                self.y_momentum = -12

        # add gravity
        self.y_momentum += 1
        if self.y_momentum > 12:
            self.y_momentum = 12
        Character.dy += self.y_momentum

        bottom_collision = False

        # deals collision
        for block in blocks_list:
            if block.colliderect((self.rect.x + Character.dx, self.rect.y, self.width, self.height)):
                Character.dx = 0

            if block.colliderect(self.rect.x, self.rect.y + Character.dy, self.width, self.height):
                if self.y_momentum < 0:
                    # self.rect.top = block.bottom
                    Character.dy = block.bottom - self.rect.top
                    # self.y_momentum = 0

                elif self.y_momentum >= 0:
                    # self.rect.bottom = block.top
                    Character.dy = block.top - self.rect.bottom
                    # self.y_momentum = 0
                    bottom_collision = True

        p_block_collision = push.update()

        print(self.air_timer)

        if bottom_collision or p_block_collision:
            self.y_momentum = 0
            self.air_timer = 0
        else:
            self.air_timer += 1



        # dy += self.y_momentum

        ####

        ####

        self.rect.x += Character.dx
        self.rect.y += Character.dy



        if type == "fb":
            game.screen.blit(self.fb, self.rect)
        else:
            game.screen.blit(self.wg, self.rect)

        pygame.draw.rect(game.screen, (255, 255, 255), self.rect, 2)

    def rt_momentum(self):
        return self.y_momentum


class FireBoy(Character):
    def __init__(self, x, y):
        self.fb = pygame.image.load("img/fireBoy.png")
        self.rect = self.fb.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.fb.get_width()
        self.height = self.fb.get_height()

        super().__init__(x, y)

    def rt_rect(self):
        return self.rect

    def rt_img(self):
        return self.fb


class WaterGirl(Character):
    def __init__(self, x, y):
        self.wg = pygame.image.load("img/waterGirl.png")

        self.rect = self.wg.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.wg.get_width()
        self.height = self.wg.get_height()
        super().__init__(x, y)

    def rt_rect(self):
        return self.rect

    def rt_img(self):
        return self.wg
