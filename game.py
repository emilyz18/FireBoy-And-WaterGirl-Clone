import pygame
from world import *
from character import *


screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60




class Game:


    def __init__(self):

        pygame.init()
        # self.screen_width = 1020
        # self.screen_height = 680
        # self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption('game')

        self.running = True

    def game_loop(self):
        fire_boy = FireBoy(60, screen_height - 140)
        # world.load_images()

        while self.running:
            clock.tick(fps)
            world = World()
            screen.fill((169, 169, 169))
            world.draw_grid()
            world.draw_blocks(screen)




            fire_boy.move("fb")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()

