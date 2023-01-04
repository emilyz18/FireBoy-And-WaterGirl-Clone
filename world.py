import pygame

import game
from game import *

tile_size = 34


class World:
    blocks_displayed = []

    def __init__(self):
        # global tile_size

        # 1, 2 ,3 top blocks
        # 4, 5, 6 bottom block variants
        self.world_data = [
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],  # 0
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0, 0, 6],

            [5, 0, 0, 0, 0, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 0, 0, 5],

            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],

            [6, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [5, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [4, 5, 6, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 7, 7, 3, 1, 8, 8, 1, 2, 3, 1, 0, 0, 0, 0, 0, 0, 4],

            [6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 0, 0, 0, 0, 0, 6],

            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],

            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 6, 4],
            [5, 2, 3, 1, 2, 3, 1, 2, 3, 7, 7, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 5, 6, 4, 5],
            [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6],  # 15

        ]

        self.load_images()

    def load_images(self):
        self.block_middle = pygame.image.load("img/blockMiddle.png")
        self.block_right = pygame.image.load("img/blockRight.png")
        self.block_three = pygame.image.load("img/block3.png")
        self.block_bottom = pygame.image.load("img/blockBottom.png")  # bottom dirt varient 1
        self.block_bottom2 = pygame.image.load("img/blockBottom2.png")  # bottom dirt varient 2
        self.block_bottom3 = pygame.image.load("img/blockBottom3.png")  # bottom dirt varient 3
        self.lava_img = pygame.image.load("img/lava.png")
        self.water_img = pygame.image.load("img/water.png")

    # def draw_grid(self, screen, s_w, s_h):
    #     for line in range(0, 30):
    #         pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, s_h))
    #
    #         for line2 in range(0, 20):
    #             pygame.draw.line(screen, (255, 255, 255), (0, line2 * tile_size), (s_w, line2 * tile_size))

    def draw_grid(self):
        for line in range(0, 30):
            pygame.draw.line(game.screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, game.screen_height))

            for line2 in range(0, 20):
                pygame.draw.line(game.screen, (255, 255, 255), (0, line2 * tile_size), (game.screen_width, line2 * tile_size))

    def draw_blocks(self, screen):
        World.blocks_displayed.clear()
        row_count = 0
        for row in self.world_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.block_middle, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    screen.blit(img, img_rect)
                    World.blocks_displayed.append(img_rect)
                if tile == 2:
                    img = pygame.transform.scale(self.block_right, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    screen.blit(img, img_rect)
                    World.blocks_displayed.append(img_rect)
                if tile == 3:
                    img = pygame.transform.scale(self.block_three, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    screen.blit(img, img_rect)
                    World.blocks_displayed.append(img_rect)
                if tile == 4:
                    img = pygame.transform.scale(self.block_bottom, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    screen.blit(img, img_rect)
                    World.blocks_displayed.append(img_rect)
                if tile == 5:
                    img = pygame.transform.scale(self.block_bottom2, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    screen.blit(img, img_rect)
                    World.blocks_displayed.append(img_rect)
                if tile == 6:
                    img = pygame.transform.scale(self.block_bottom3, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    screen.blit(img, img_rect)
                    World.blocks_displayed.append(img_rect)
                if tile == 7:
                    img = pygame.transform.scale(self.lava_img, (tile_size, tile_size - 8))
                    img_rect = img.get_rect()

                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size + 8
                    screen.blit(img, (img_rect.x, img_rect.y))
                    # pygame.draw.rect(screen, (255, 255, 255), img_rect, 2)
                if tile == 8:
                    img = pygame.transform.scale(self.water_img, (tile_size, tile_size - 8))
                    img_rect = img.get_rect()

                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size + 8
                    screen.blit(img, (img_rect.x, img_rect.y))
                        # pygame.draw.rect(screen, (255, 255, 255), img_rect, 2)
                    World.blocks_displayed.append(img_rect)
                col_count += 1
            row_count += 1
            print(len(World.blocks_displayed))
