import pygame
from world import *
from character import *



screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

class Game:
    def __init__(self):

        pygame.init()
        self.screen_width = 1020
        self.screen_height = 680
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        pygame.display.set_caption('game')

        self.running = True

    def game_loop(self):
        while self.running:
            world = World()
            world.load_images()
            self.screen.fill((169, 169, 169))

            world.draw_grid(self.screen, self.screen_width, self.screen_height)

            world.draw_blocks(self.screen)
            fire_boy = FireBoy(40, screen_height - 140)
            fire_boy.move()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()
