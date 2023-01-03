import pygame


class Control:
    def __init__(self):
        self.y_momentum = 0
        self.jumped = False

    def move(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5
        if key[pygame.K_SPACE]:
            self.y_momentum = -15
            self.jumped = True


        self.y_momentum += 1
        if self.y_momentum > 10:
            self.y_momentum = 10
        dy += self.y_momentum

        listt = []
        listt.append(dx)
        listt.append(dy)

        return listt


class FireBoyControl(Control):
    def __init__(self):
        super().__init__()


class WaterGirlControl(Control):
    def __init__(self):
        super().__init__()
