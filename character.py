import pygame

from control import *
from game import *
from world import *
from world import World


class Character:
    def __init__(self, x, y):
        self.y_momentum = 0
        self.character = pygame.image.load("img/characterTemp.png")

        self.rect = self.character.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.air_timer = 0
        self.width = self.character.get_width()
        self.height = self.character.get_height()

    def draw(self):
        game.screen.blit(self.character, self.rect)

    def move(self, type):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if type == "fb":
            controls = [key[pygame.K_LEFT], key[pygame.K_RIGHT], key[pygame.K_UP]]
        if type == "wg":
            controls = [key[pygame.K_a], key[pygame.K_d], key[pygame.K_w]]

        if controls[0]:  # left
            dx -= 10
        if controls[1]:  # right
            dx += 10
        if controls[2]:  # jump
            if self.air_timer < 5:
                self.y_momentum = -10

        # add gravity
        self.y_momentum += 1
        if self.y_momentum > 1112:
            self.y_momentum = 1112
        dy += self.y_momentum

        bottom_collision = False

        # deals collision
        for block in World.blocks_displayed:
            if block.colliderect((self.rect.x + dx, self.rect.y, self.width, self.height)):
                dx = 0
            if block.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.y_momentum < 0:
                    # self.rect.top = block.bottom
                    dy = block.bottom - self.rect.top
                    # self.y_momentum = 0

                elif self.y_momentum >= 0:
                    # self.rect.bottom = block.top
                    dy = block.top - self.rect.bottom
                    # self.y_momentum = 0
                    bottom_collision = True

        if bottom_collision:
            self.y_momentum = 0
            self.air_timer = 0
        else:
            self.air_timer += 1

        # dy += self.y_momentum

        self.rect.x += dx
        self.rect.y += dy

        game.screen.blit(self.character, self.rect)
        pygame.draw.rect(game.screen, (255, 255, 255), self.rect, 2)


class FireBoy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)


class WaterGirl(Character):
    def __init__(self):
        super()
