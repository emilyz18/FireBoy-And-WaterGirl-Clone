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

    def game_loop(self):

        water_girl = WaterGirl(50, screen_height - 140)
        fire_boy = FireBoy(50, screen_height - 140)

        push = Push(4 * 34, 17 * 34, fire_boy, water_girl)
        # tramp = Tramp(27 * 34, 15 * 34, fire_boy, water_girl)
        # speeder = Speeder(17 * 34, 17 * 34, fire_boy, water_girl)
        # speeder2 = Speeder(10 * 34, 17 * 34, fire_boy, water_girl)

        # world.load_images()
        world = World(screen, fire_boy, water_girl)
        # world.draw_blocks(screen, fire_boy, water_girl, push)
        # img = pygame.image.load("img/blockMiddle.png")
        # rect = img.get_rect()
        # screen.blit(img, rect)

        # world.draw_grid(screen, screen_width, screen_height)
        # print(world)

        while self.running:
            clock.tick(fps)
            # world = World()
            # print(world)
            screen.fill((169, 169, 169))
            # world.draw_grid(screen, screen_width, screen_height)
            world.draw_blocks(screen, fire_boy, water_girl, push)

            # if pygame.sprite.spritecollide(fire_boy, world.coin_group, True):
            #     self.score += 1
            # self.draw_text("X " + str(self.score), pygame.font.SysFont("Bauhaus 93", 30), (255, 255, 255),
            #                tile_size - 10, 10)
            #
            # world.coin_group.draw(screen)



            # tramp.draw()
            # speeder.draw(screen)
            # speeder2.draw("left")

            # water_girl.move("wg")
            # fire_boy.move("fb")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        game.screen.blit(img, (x, y))

