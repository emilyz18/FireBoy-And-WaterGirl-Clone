import sys

import data
from Button import Button
from push import Push
from world import *
from world import World
from push import *

screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 60

BG = pygame.image.load("img/Background.png")

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

        self.world_data1 = data.data1

        self.world_data2 = data.data2

        self.world_data3 = data.data3

    def game_loop(self):

        while self.running:
            self.main_menu()
            clock.tick(fps)
            screen.fill((169, 169, 169))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()

    def get_font(self, size):
        return pygame.font.Font("img/font.ttf", size)

    def main_menu(self):
        while True:
            screen.blit(BG, (0, 0))
            img = self.get_font(43).render("Hydrogirl and Lavaboy", True, (255, 255, 255))
            game.screen.blit(img, (60, 90))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            font_size = 44


            lv1_button = Button(image=pygame.image.load("img/buttonLabel.png"), pos=(520, 265),
                                text_input="Level 1", font=self.get_font(font_size), base_color="#d7fcd4",
                                hovering_color="White")

            lv2_button = Button(image=pygame.image.load("img/buttonLabel.png"), pos=(520, 415),
                                text_input="Level 2", font=self.get_font(font_size), base_color="#d7fcd4",
                                hovering_color="White")

            lv3_button = Button(image=pygame.image.load("img/buttonLabel.png"), pos=(520, 555),
                                text_input="Level 3", font=self.get_font(font_size), base_color="#d7fcd4",
                                hovering_color="White")

            # screen.blit(MENU_TEXT, MENU_RECT)

            for button in [lv1_button, lv2_button, lv3_button]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if lv1_button.checkForInput(MENU_MOUSE_POS):
                        self.play1()
                    if lv2_button.checkForInput(MENU_MOUSE_POS):
                        self.play2()
                    if lv3_button.checkForInput(MENU_MOUSE_POS):
                        self.play3()

            pygame.display.update()

    def play1(self):
        water_girl1 = WaterGirl(screen_width - 3 * 34 + 17, 34)
        fire_boy1 = FireBoy(2 * 34 - 17, 34)

        push = Push(3 * 34, 14 * 34, fire_boy1, water_girl1)

        world = World(fire_boy1, water_girl1, self.world_data1, push)

        while self.running:
            clock.tick(fps)
            screen.fill((169, 169, 169))

            # world.draw_grid(screen, screen_width, screen_height)
            game_over = world.draw_blocks(screen, fire_boy1, water_girl1, False)
            if game_over:
                del water_girl1
                del fire_boy1
                del push
                del world
                self.play1()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()

    def play2(self):
        water_girl2 = WaterGirl(50, screen_height - 140)
        fire_boy2 = FireBoy(50, screen_height - 140)

        push = Push(4 * 34, 10 * 34, fire_boy2, water_girl2)

        world = World(fire_boy2, water_girl2, self.world_data2, push)
        # print(test)

        while self.running:
            clock.tick(fps)
            screen.fill((169, 169, 169))

            # world.draw_grid(screen, screen_width, screen_height)
            game_over = world.draw_blocks(screen, fire_boy2, water_girl2, False)
            if game_over:
                del water_girl2
                del fire_boy2
                del push
                del world
                self.play2()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()

    def play3(self):
        water_girl3 = WaterGirl(screen_width - 3 * 34 + 17, screen_height - 3 * 34)
        fire_boy3 = FireBoy(2 * 34 - 17, screen_height - 3 * 34)

        push = Push(7 * 34, 17 * 34, fire_boy3, water_girl3)

        world = World(fire_boy3, water_girl3, self.world_data3, push)
        # print(test)

        while self.running:
            clock.tick(fps)
            screen.fill((169, 169, 169))

            # world.draw_grid(screen, screen_width, screen_height)
            game_over = world.draw_blocks(screen, fire_boy3, water_girl3, False)
            if game_over:
                del water_girl3
                del fire_boy3
                del push
                del world
                self.play3()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

        pygame.quit()
