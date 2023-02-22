import pygame

from push import Push
# from character import WaterGirl
from world import *
from character import *
from world import World
from push import *

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60



class Game:


    def __init__(self):
        self.score = 0

        pygame.init()
        # self.screen_width = 1020
        # self.screen_height = 680
        # self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption('game')
        # self.score = 0

        self.running = True

        self.world_data = [
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],  # 0
            [6, 0, 20, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [4, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 6],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [4, 0, 0, 0, 0, 0, 0, 11, 0, 0, 10, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0, 0, 6],

            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],

            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],

            [6, 1, 2, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [5, 6, 4, 0, 0, 0, 0, 0, 1, 2, 3, 1, 2, 8, 8, 8, 1, 8, 8, 8, 3, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 2, 1, 0, 0, 0, 0, 0, 0, 4],

            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 6],

            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],

            [4, 0, 0, 0, 0, 0, 16, 0, 17, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 12, 12, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 5, 6, 4, 5],
            [4, 3, 1, 2, 3, 1, 7, 7, 7, 2, 3, 1, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1, 2, 3, 6, 4, 6, 5],  # 15

        ]

    def game_loop(self):

        water_girl = WaterGirl(50, screen_height - 140)
        fire_boy = FireBoy(50, screen_height - 140)

        push = Push(4 * 34, 17 * 34, fire_boy, water_girl)

        world = World(screen, fire_boy, water_girl, self.world_data, push)
        # world.draw_blocks(screen, fire_boy, water_girl, push)

        # world.draw_grid(screen, screen_width, screen_height)
        # print(world)

        while self.running:
            clock.tick(fps)
            screen.fill((169, 169, 169))
            world.draw_grid(screen, screen_width, screen_height)
            world.draw_blocks(screen, fire_boy, water_girl)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()

