import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Doom Fire')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
