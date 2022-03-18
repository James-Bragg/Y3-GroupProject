import math
import pygame
import random
pygame.init()

class GUIVisualInfo:
    Black = 0, 0, 0
    White = 255, 255 , 255
    Green = 0, 255, 0
    Blue = 0, 0, 255
    Red = 255, 0, 0
    BackgroundColor = Black

    Gradient = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    Font = pygame.font.SysFont('Arial', 30)
    BFont = pygame.font.SysFont('Arial', 40)
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
        self.DataBlockHeight = math.floor((self.height - self.TopBorder) / (self.maxVal - self.minVal))
        self.initializeX = self.Margin // 2


def draw(drawInfo):
    drawInfo.window.fill(drawInfo.BackgroundColor)

    controls = drawInfo.Font.render("Key: R = reset, Space = Start visualizer, A = Ascending, D = Descending", 1, drawInfo.White)
    drawInfo.window.blit(controls, (drawInfo.width/2 - controls.get_width()/2, 10))

    drawList(drawInfo)
    pygame.display.update()

def drawList(drawInfo, colourPositions={}, clearBG=False):
    lst = drawInfo.lst

    if clearBG:
        clearRect = (drawInfo.Margin//2, drawInfo.TopBorder,
         drawInfo.width - drawInfo.Margin, drawInfo.height - drawInfo.TopBorder)
        pygame.draw.rect(drawInfo.window, drawInfo.BackgroundColor, clearRect)

    for i, val in enumerate(lst):
        x = drawInfo.initializeX + i * drawInfo.DataBlockWidth
        y = drawInfo.height - (val - drawInfo.minVal) * drawInfo.DataBlockHeight

        colour = drawInfo.Gradient[i % 3]

        if i in colourPositions:
            colour = colourPositions[i]

        pygame.draw.rect(drawInfo.window, colour, (x, y, drawInfo.DataBlockWidth, drawInfo.height))

    if clearBG:
        pygame.display.update()

def GenerateStartingData(n, minVal, maxVal):
    lst = []

    for _ in range (n):
        val = random.randint(minVal, maxVal)
        lst.append(val)

    return lst

def bubbleSort(drawInfo, ascending = True):
    lst = drawInfo.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                drawList(drawInfo, {j: drawInfo.Green, j + 1: drawInfo.Red}, True)
                yield True

    return lst

def main():
    active = True
    clock = pygame.time.Clock()

    n = 50
    minVal = 0
    maxVal = 100

    lst = GenerateStartingData(n, minVal, maxVal)
    GUI = GUIVisualInfo(800, 600, lst)
    sorting = False
    ascending = True

    sortingAlgorithm = bubbleSort
    sortingAlgorithmName = "bubble Sort"
    sortingAlgorithmGenerator = None

    while active:
        #clock.tick(60)

        if sorting:
            try:
                next(sortingAlgorithmGenerator)
            except StopIteration:
                sorting = False
        else:
            draw(GUI)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = GenerateStartingData(n, minVal, maxVal)
                GUI.setList(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sortingAlgorithmGenerator = sortingAlgorithm(GUI, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
    pygame.quit

if __name__ == '__main__':
    main()


