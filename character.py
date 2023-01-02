import pygame
from game import *

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))


class Character:
    def __init__(self, x, y):
        self.y_momentum = 0
        self.character = pygame.image.load("img/characterTemp.png")

        self.rect = self.character.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):

        # get key presses
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.y_momentum = - 15
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            print("right")
            dx += 5

        self.y_momentum += 1  # how fast it falls
        if self.y_momentum > 10:
            self.y_momentum = 10
        dy += self.y_momentum

        # if not keys[pygame.K_IGHT] and keys[pygame.K_LEFT]:
        #     pass
        # elif not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        #     pass
        # else:
        #     dx = 0
        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.character, self.rect)

        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)



class FireBoy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)


class WaterGirl(Character):
    def __init__(self):
        super()
