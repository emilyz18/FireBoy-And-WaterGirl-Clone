import pygame

tile_size = 34


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, type, screen):
        type.draw(screen)


class Lava(Obstacle):
    def __init__(self, x, y):
        self.lava_image = pygame.image.load("img/lava.png")
        self.image = pygame.transform.scale(self.lava_image, (tile_size, tile_size - 8))
        super().__init__(x, y)


class Water(Obstacle):
    def __init__(self, x, y):
        self.water_image = pygame.image.load("img/water.png")
        self.image = pygame.transform.scale(self.water_image, (tile_size, tile_size - 8))
        super().__init__(x, y)


class Slime(Obstacle):
    def __init__(self, x, y):
        self.slime_image = pygame.image.load("img/slime.png")
        self.image = pygame.transform.scale(self.slime_image, (tile_size, tile_size - 8))
        super().__init__(x, y)


class Wall(Obstacle):
    def __init__(self, x, y):
        self.wall_image = pygame.image.load("img/wall.png")
        self.image = pygame.transform.scale(self.wall_image, (tile_size - 12, tile_size * 2))
        super().__init__(x, y)
