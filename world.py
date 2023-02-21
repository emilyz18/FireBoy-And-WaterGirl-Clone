import pygame

from obstacle import *
from character import *
from push import Push
# from tramp import Tramp

# from push import *

tile_size = 34


class World:
    collision_blocks = []
    # horizontal_buttons = []
    render_blocks = [] # collision blocks in tuple format

    # p_block = []

    def __init__(self, screen, fb, wg):
        self.block_x = 34 * 4
        self.lava_group = pygame.sprite.Group()
        self.water_group = pygame.sprite.Group()
        self.slime_group = pygame.sprite.Group()
        self.speeder_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.redGem_group = pygame.sprite.Group()
        self.blueGem_group = pygame.sprite.Group()


        self.vertical_button_pressed = False
        self.horizontal_button_pressed = False
        self.horizontal_buttons = []
        self.vertical_buttons = []

        self.coin_score = 0

        # self.purple_button = []
        # global tile_size

        # 1, 2 ,3 top blocks
        # 4, 5, 6 bottom block variants
        # 7 fire
        # 8 water
        # 9 slime
        # 10 wall
        # 11 vertical button
        # 12 right speeders
        # 13 left speeders
        # 14 hwall
        # 15 hbutton
        # 16 coin
        # 17 red gem
        # 18 blue gem
        self.world_data = [
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],  # 0
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [4, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 6],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [4, 0, 0, 0, 0, 0, 0, 11, 0, 0, 10, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 0, 0, 6],

            [5, 0, 0, 0, 0, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 0, 0, 5],

            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],

            [6, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
            [5, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 5],
            [4, 5, 6, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 7, 7, 3, 1, 8, 8, 1, 9, 9, 1, 0, 0, 0, 0, 0, 0, 4],

            [6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 1, 1, 0, 14, 0, 6],

            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],

            [4, 0, 0, 0, 0, 0, 16, 0, 17, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 0, 0, 0, 15, 0, 0, 0, 0, 4, 5, 6, 4],
            [5, 2, 3, 1, 2, 3, 1, 2, 3, 7, 7, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 5, 6, 4, 5],
            [4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6],  # 15

        ]

        self.load_images()
        row_count = 0
        for row in self.world_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.block_middle, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    World.render_blocks.append(tile)
                    World.collision_blocks.append(img_rect)
                if tile == 2:
                    img = pygame.transform.scale(self.block_right, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    World.render_blocks.append(tile)
                    World.collision_blocks.append(img_rect)
                if tile == 3:
                    img = pygame.transform.scale(self.block_three, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # screen.blit(img, img_rect)
                    tile = (img, img_rect)
                    World.render_blocks.append(tile)
                    World.collision_blocks.append(img_rect)
                if tile == 4:
                    img = pygame.transform.scale(self.block_bottom, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # screen.blit(img, img_rect)
                    # World.blocks_displayed.append(img_rect)
                    tile = (img, img_rect)
                    World.render_blocks.append(tile)
                    World.collision_blocks.append(img_rect)
                if tile == 5:
                    img = pygame.transform.scale(self.block_bottom2, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # screen.blit(img, img_rect)
                    # World.blocks_displayed.append(img_rect)
                    tile = (img, img_rect)
                    World.render_blocks.append(tile)
                    World.collision_blocks.append(img_rect)
                if tile == 6:
                    img = pygame.transform.scale(self.block_bottom3, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # screen.blit(img, img_rect)
                    # World.blocks_displayed.append(img_rect)
                    tile = (img, img_rect)
                    World.render_blocks.append(tile)
                    World.collision_blocks.append(img_rect)
                if tile == 7:
                    lava = Lava(col_count * tile_size, row_count * tile_size + 8)
                    self.lava_group.add(lava)
                if tile == 8:
                    water = Water(col_count * tile_size, row_count * tile_size + 8)
                    self.water_group.add(water)
                if tile == 9:
                    slime = Slime(col_count * tile_size, row_count * tile_size + 8)
                    self.slime_group.add(slime)
                if tile == 12:
                    speeder = Speeder(col_count * tile_size, row_count * tile_size + 10, fb, wg, "right")
                    self.speeder_group.add(speeder)
                if tile == 13:
                    speeder = Speeder(col_count * tile_size, row_count * tile_size + 10, fb, wg, "left")
                    self.speeder_group.add(speeder)
                    # speeder.draw(self.speeder_group, screen)
                if tile == 16:
                    coin = Coin(col_count * tile_size, row_count * tile_size)
                    self.coin_group.add(coin)
                    # coin.draw(self.coin_group, screen)

                if tile == 17:
                    rg = RedGem(col_count * tile_size, row_count * tile_size)
                    self.redGem_group.add(rg)

                if tile == 18:
                    bg = BlueGem(col_count * tile_size, row_count * tile_size)
                    self.blueGem_group.add(bg)

                col_count += 1
            row_count += 1

    def load_images(self):
        self.block_middle = pygame.image.load("img/blockMiddle.png")
        self.block_right = pygame.image.load("img/blockRight.png")
        self.block_three = pygame.image.load("img/block3.png")
        self.block_bottom = pygame.image.load("img/blockBottom.png")  # bottom dirt varient 1
        self.block_bottom2 = pygame.image.load("img/blockBottom2.png")  # bottom dirt varient 2
        self.block_bottom3 = pygame.image.load("img/blockBottom3.png")  # bottom dirt varient 3
        self.wall = pygame.image.load("img/wall.png")
        self.vertical_button = pygame.image.load("img/button.png")
        self.block = pygame.image.load("img/block.png")

        self.horizontal_wall = pygame.image.load("img/hwall.png")
        self.horizontal_button = pygame.image.load("img/hbutton.png")

    def draw_grid(self, screen, w, h):
        for line in range(0, 30):
            pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0),
                             (line * tile_size, h))

            for line2 in range(0, 20):
                pygame.draw.line(screen, (255, 255, 255), (0, line2 * tile_size),
                                 (w, line2 * tile_size))

    def draw_blocks(self, screen, fb, wg, push):
        # World.blocks_displayed.clear()
        # self.horizontal_buttons.clear()
        # World.vertical_buttons.clear()

        # World.render_blocks.clear()

        # World.collision_blocks.clear()
        vertical_list = []
        horizontal_list = []


        row_count = 0
        for row in self.world_data:
            col_count = 0
            for tile in row:
                if tile == 10:
                    # wall = Wall(col_count * tile_size, row_count * tile_size - 34)
                    # self.wall_group.add(wall)
                    # wall.draw(self.wall_group, screen)
                    # # World.blocks_displayed.append(wall.get_rect())

                    img = pygame.transform.scale(self.wall, (tile_size - 12, tile_size * 2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size - 34

                    self.check_button_v_press(fb, wg, "vertical")

                    if self.vertical_button_pressed:
                        img_rect.x = -100
                        img_rect.y = -100

                    screen.blit(img, (img_rect.x, img_rect.y))
                    pygame.draw.rect(screen, (255, 255, 255), img_rect, 2)
                    # World.blocks_displayed.append(img_rect)
                    # tile = (img, img_rect)
                    # World.render_blocks.append(tile)
                    vertical_list.append(img_rect)
                if tile == 11:
                    img = pygame.transform.scale(self.vertical_button, (tile_size + 4, tile_size / 2 - 2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size + tile_size / 2 + 2
                    screen.blit(img, (img_rect.x, img_rect.y))

                    self.vertical_buttons.append(img_rect)

                    # World.blocks_displayed.append(img_rect)
                    # tile = (img, img_rect)
                    # World.render_blocks.append(tile)

                if tile == 14:
                    img = pygame.transform.scale(self.horizontal_wall, (tile_size * 2, tile_size - 12))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size + 14

                    self.check_button_v_press(fb, wg, "horizontal")

                    if self.horizontal_button_pressed:
                        img_rect.y = row_count * tile_size + 14 + 88  # 88 is max levitation height

                    screen.blit(img, (img_rect.x, img_rect.y))
                    pygame.draw.rect(screen, (255, 255, 255), img_rect, 2)
                    horizontal_list.append(img_rect)

                if tile == 15:
                    img = pygame.transform.scale(self.horizontal_button, (tile_size + 4, tile_size / 2 - 2))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size + 4
                    img_rect.y = row_count * tile_size + tile_size / 2 + 2
                    screen.blit(img, (img_rect.x, img_rect.y))
                    self.horizontal_buttons.append(img_rect)

                col_count += 1
            row_count += 1

        for tile in World.render_blocks:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

        if pygame.sprite.spritecollide(fb, self.coin_group, True) or pygame.sprite.spritecollide(wg, self.coin_group, True):
            self.coin_score += 1


        self.draw_text("X " + str(self.coin_score), pygame.font.SysFont("Bauhaus 93", 30), (255, 255, 255),
                       tile_size - 10, 10)


        self.lava_group.draw(screen)
        self.water_group.draw(screen)
        self.slime_group.draw(screen)
        self.speeder_group.draw(screen)

        self.coin_group.draw(screen)
        self.redGem_group.draw(screen)
        self.blueGem_group.draw(screen)

        # draw players
        combined = self.collision_blocks + vertical_list + horizontal_list
        fb.move(combined, push, self.speeder_group)
        wg.move(combined, push, self.speeder_group)

    def check_button_v_press(self, fb, wg, type):

        fb_rect = fb.rt_rect()
        wg_rect = wg.rt_rect()
        if type == "vertical":
            if self.vertical_button_pressed == True:
                self.vertical_button_pressed = False
            for block in self.vertical_buttons:
                if block.colliderect(fb_rect) or block.colliderect(wg_rect):
                    self.vertical_button_pressed = True
            self.vertical_buttons.clear()  # must be added here
        if type == "horizontal":
            if self.horizontal_button_pressed == True:
                self.horizontal_button_pressed = False
            for block in self.horizontal_buttons:
                if block.colliderect(fb_rect) or block.colliderect(wg_rect):
                    self.horizontal_button_pressed = True
            self.horizontal_buttons.clear()  # must be added here

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        game.screen.blit(img, (x, y))


