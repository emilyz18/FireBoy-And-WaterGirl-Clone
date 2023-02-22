import pygame

import game
from game import *


# from world import World


class Character:
    # dx = 0
    # dy = 0

    fb_dx = 0
    fb_dy = 0

    wg_dx = 0
    wg_dy = 0

    fb_air_timer = 0
    wg_air_timer = 0

    fb_momentum = 0

    def __init__(self, x, y):
        # self.block = pygame.image.load("img/block.png")
        # self.img_rect = self.block.get_rect()
        # self.img_rect.x = x
        # self.img_rect.y = y
        self.score = 0
        pass

    # def draw(self):
    # game.screen.blit(self.fb, self.rect)
    # game.screen.blit(self.wg, self.rect)


class FireBoy(Character):
    def __init__(self, x, y):
        self.fb = pygame.image.load("img/fireBoy.png")
        self.rect = self.fb.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.fb.get_width()
        self.height = self.fb.get_height()

        self.y_momentum = 0
        # self.air_timer = 0

        super().__init__(x, y)

    def rt_rect(self):
        return self.rect

    def rt_img(self):
        return self.fb

    def rt_momentum(self):
        return self.y_momentum

    def move(self, blocks_list, push, speeder_group):

        Character.fb_dx = 0
        Character.fb_dy = 0
        key = pygame.key.get_pressed()
        # if type == "fb":
        #     controls = [key[pygame.K_LEFT], key[pygame.K_RIGHT], key[pygame.K_UP]]
        # if type == "wg":
        #     controls = [key[pygame.K_a], key[pygame.K_d], key[pygame.K_w]]

        if key[pygame.K_a]:  # left
            Character.fb_dx -= 7
        if key[pygame.K_d]:  # right
            Character.fb_dx += 7
        if key[pygame.K_w]:  # jump
            if Character.fb_air_timer < 5:
                self.y_momentum = -10

        # add gravity
        self.y_momentum += 1
        if self.y_momentum > 12:
            self.y_momentum = 12
        Character.fb_dy += self.y_momentum

        bottom_collision = False

        p_rect = push.rt_rect()
        p_dx = push.rt_dx()


        # deals collision
        for block in blocks_list:
            if block.colliderect((self.rect.x + Character.fb_dx, self.rect.y, self.width, self.height)):
                Character.fb_dx = 0

            if block.colliderect(self.rect.x, self.rect.y + Character.fb_dy, self.width, self.height):
                if self.y_momentum < 0:
                    # self.rect.top = block.bottom
                    Character.fb_dy = block.bottom - self.rect.top
                    # self.y_momentum = 0

                elif self.y_momentum >= 0:
                    # self.rect.bottom = block.top
                    Character.fb_dy = block.top - self.rect.bottom
                    # self.y_momentum = 0
                    bottom_collision = True

        p_block_collision = push.update(blocks_list, "fb")
        # vent_block_collision = vent.turn_on("fb")

        for speeder in speeder_group:
            speeder_block_collision = speeder.turn_on("fb")
            if speeder_block_collision:
                break

        if bottom_collision or p_block_collision or speeder_block_collision:
        # if bottom_collision or p_block_collision or vent_block_collision or speeder_block_collision:

            self.y_momentum = 0
            Character.fb_air_timer = 0
        else:
            Character.fb_air_timer += 1

        # method 2: decrease jump height #################################
        # for speeder in speeder_group:
        #     speeder_block_collision = speeder.turn_on("fb")
        #
        #
        #
        #     if bottom_collision or p_block_collision or vent_block_collision or speeder_block_collision:
        #         self.y_momentum = 0
        #         Character.fb_air_timer = 0
        #     else:
        #         Character.fb_air_timer += 1
        #################################################################

        # dy += self.y_momentum

        self.rect.x += Character.fb_dx
        self.rect.y += Character.fb_dy

        game.screen.blit(self.fb, self.rect)

        pygame.draw.rect(game.screen, (255, 255, 255), self.rect, 2)


class WaterGirl(Character):
    def __init__(self, x, y):
        self.wg = pygame.image.load("img/waterGirl.png")

        self.rect = self.wg.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.wg.get_width()
        self.height = self.wg.get_height()
        super().__init__(x, y)

        self.y_momentum = 0
        # self.air_timer = 0

    def rt_rect(self):
        return self.rect

    def rt_img(self):
        return self.wg

    def rt_momentum(self):
        return self.y_momentum

    def move(self, blocks_list, push, speeder_group):
        Character.wg_dx = 0
        Character.wg_dy = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:  # left
            Character.wg_dx -= 7
        if key[pygame.K_RIGHT]:  # right
            Character.wg_dx += 7
        if key[pygame.K_UP]:  # jump
            if self.wg_air_timer < 5:
                self.y_momentum = -10

        # add gravity
        self.y_momentum += 1
        if self.y_momentum > 12:
            self.y_momentum = 12
        Character.wg_dy += self.y_momentum

        bottom_collision = False

        p_rect = push.rt_rect()
        p_dx = push.rt_dx()

        # deals collision
        for block in blocks_list:
            if block.colliderect((self.rect.x + Character.wg_dx, self.rect.y, self.width, self.height)):
                Character.wg_dx = 0

            if block.colliderect(self.rect.x, self.rect.y + Character.wg_dy, self.width, self.height):
                if self.y_momentum < 0:
                    # self.rect.top = block.bottom
                    Character.wg_dy = block.bottom - self.rect.top
                    # self.y_momentum = 0

                elif self.y_momentum >= 0:
                    # self.rect.bottom = block.top
                    Character.wg_dy = block.top - self.rect.bottom
                    # self.y_momentum = 0
                    bottom_collision = True

        p_block_collision = push.update(blocks_list, "wg")
        # vent_block_collision = vent.turn_on("wg")
        for speeder in speeder_group:
            speeder_block_collision = speeder.turn_on("wg")
            if speeder_block_collision:
                break

        if bottom_collision or p_block_collision or speeder_block_collision:
        # if bottom_collision or p_block_collision or vent_block_collision or speeder_block_collision:

            self.y_momentum = 0
            self.wg_air_timer = 0
        else:
            self.wg_air_timer += 1

        # dy += self.y_momentum

        self.rect.x += Character.wg_dx
        self.rect.y += Character.wg_dy

        game.screen.blit(self.wg, self.rect)

        pygame.draw.rect(game.screen, (255, 255, 255), self.rect, 2)
