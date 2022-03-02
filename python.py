import pygame
import random
pygame.init()

class GUIVisualInfo:
    Black = 0, 0, 0
    White = 255, 255 , 255
    Green = 0, 255, 0
    blue = 0, 0, 255
    red = 255, 0, 0
    grey = 128, 128, 128
    BackgroundColor = Black

    Margin = 100
    TopBorder = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Algorithm visualizer")
        self.setList(lst)

    def setList(self, lst):
        self.lst = lst
        self.minVal = min(lst)
        self.maxVal = max(lst)

        self.DataBlockWidth = round((self.width - self.Margin) / len(lst))
        self.DataBlockWidth = round((self.height - self.TopBorder) / (self.maxVal - self.minVal))
        self.initializeX = self.Margin // 2


def GenerateStartingData(n, minVal, maxVal):
    lst = []

    for _ in range (n):
        val = random.randint(minVal, maxVal)
        lst.append(val)

    return lst


def main():
    active = True
    clock = pygame.time.Clock()

    n = 50
    minVal = 0
    maxVal = 100

    lst = GenerateStartingData(n, minVal, maxVal)
    GUI = GUIVisualInfo(800, 600, lst)

    pygame.display.update()

    while active:
        clock.tick(165)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                active = False
    
    pygame.quit

if __name__ == '__main__':
    main()
