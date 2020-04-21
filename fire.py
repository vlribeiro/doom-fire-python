import pygame
import sys
import random
from pygame.locals import *


class Fire:
    colors = [
        (7,   7,   7),
        (31,  7,   7),
        (47,  15,  7),
        (71,  15,  7),
        (87,  23,  7),
        (103, 31,  7),
        (119, 31,  7),
        (143, 39,  7),
        (159, 47,  7),
        (175, 63,  7),
        (191, 71,  7),
        (199, 71,  7),
        (223, 79,  7),
        (223, 87,  7),
        (223, 87,  7),
        (215, 95,  7),
        (215, 95,  7),
        (215, 103, 15),
        (207, 111, 15),
        (207, 119, 15),
        (207, 127, 15),
        (207, 135, 23),
        (199, 135, 23),
        (199, 143, 23),
        (199, 151, 31),
        (191, 159, 31),
        (191, 159, 31),
        (191, 167, 39),
        (191, 167, 39),
        (191, 175, 47),
        (183, 175, 47),
        (183, 183, 47),
        (183, 183, 55),
        (207, 207, 111),
        (223, 223, 159),
        (239, 239, 199),
        (255, 255, 255)
    ]
    max_decay = 4

    def __init__(self, width, height, pixel_size):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.virtual_width = self.width // self.pixel_size
        self.virtual_height = self.height // self.pixel_size
        self.pixel_array = [0] * \
            (self.virtual_width - 1) * self.virtual_height + \
            [len(self.colors) - 1] * self.virtual_width
        super().__init__()

    def propagate(self):
        for i, v in enumerate(self.pixel_array):
            below_index = i + self.virtual_width
            if (below_index < len(self.pixel_array)):
                decay = random.randint(0, self.max_decay)
                self.pixel_array[max(i - decay, 0)] = max(
                    [self.pixel_array[below_index] - decay, 0])

    def render(self, surface):
        for i, v in enumerate(self.pixel_array):
            pygame.draw.rect(surface, self.colors[v], Rect(
                i % self.virtual_width * self.pixel_size,
                i // self.virtual_width * self.pixel_size,
                self.pixel_size, self.pixel_size))
            pygame.draw.rect(surface, (16, 16, 16), Rect(
                i % self.virtual_width * self.pixel_size,
                i // self.virtual_width * self.pixel_size,
                self.pixel_size, self.pixel_size), 1)


class Canvas:
    bg = "#1a202c"

    def __init__(self, screen, fire):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fire = fire
        super().__init__()

    def loop(self):
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return False

        fire.propagate()
        fire.render(self.screen)

        pygame.display.update()
        return True


fire = Fire(200, 200, 8)

pygame.init()
screen = pygame.display.set_mode((fire.width, fire.height))
pygame.display.set_caption('Doom Fire')

canvas = Canvas(screen, fire)
while canvas.loop():
    pass

sys.exit()
