
import math
import pygame
pygame.init()

class GUIVisualInfo:
    # variables for colours
    Black = 42, 58, 118
    White = 255, 255 , 255
    Green = 0, 255, 0
    Blue = 0, 0, 255
    Red = 255, 0, 0
    BackgroundColor = Black

    # gradient which is used to sets colours of the column
    Gradient = [
        (46, 172, 49),
        (10, 142, 192),
        (235, 170, 18)
    ]

    # variable for font and GUI sizes
    Font = pygame.font.SysFont('Arial', 25)
    BFont = pygame.font.SysFont('Arial', 30)
    Margin = 100
    TopBorder = 150

    #sets information about the size and basic elements of the GUI
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("Algorithm visualizer")
        self.setList(lst)

    # setting list and creating GUI objects to visualize data onto the screen using the min/max values from the array
    def setList(self, lst):
        self.lst = lst
        self.minVal = min(lst)
        self.maxVal = max(lst)

        self.DataBlockWidth = round((self.width - self.Margin) / len(lst))
        self.DataBlockHeight = math.floor((self.height - self.TopBorder) / (self.maxVal - self.minVal))
        self.initializeX = self.Margin // 2
   
def main(lst, sort):

    active = True

    #passes gui information such as size and array to determine the size of columns
    GUI = GUIVisualInfo(1024, 768, lst)

    #setting default variabes 
    sorting = False
    ascending = True
    sortingAlgorithmName = sort
    sortingAlgorithmGenerator = None

    #runs while application is on
    while active:

        # tries to run the sorting algorithm if sorting is set to true
        if sorting:
            try:
                next(sortingAlgorithmGenerator)
            except StopIteration:
                sorting = False
        else:
            # else will update the display elements such as order of sorting order
            from draw_algorithms import draw_key
            draw_key.draw(GUI, sortingAlgorithmName, ascending)

        #sets key events on action or key press to interface with the display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                GUI.setList(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                from Sorting_algorthims import bubbleSort, insertionSort, selectionSort
                if sort == "Bubble Sort":
                    sortingAlgorithmGenerator = bubbleSort(GUI, lst, sort, ascending)
                elif sort == "Insertion Sort":
                    sortingAlgorithmGenerator = insertionSort(GUI, lst, sort, ascending)
                elif sort == "Selection Sort":
                    sortingAlgorithmGenerator = selectionSort(GUI, lst, sort, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
    
    pygame.quit


