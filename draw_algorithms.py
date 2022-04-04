from pygame_visualizer import *

# a class for drawing objects onto the algorithm screen
class draw_key:

    # runs a function that will get information about the pygame. Renders out the key at the top of the screen. 
    # Showing information about the system and how to operate it
    def draw(drawInfo, sortingAlgorithmName, ascending):
        drawInfo.window.fill(drawInfo.BackgroundColor)

        title = drawInfo.Font.render(f"{sortingAlgorithmName} - {'Ascending' if ascending else 'Desencding'} ", 1, drawInfo.White)
        drawInfo.window.blit(title, (drawInfo.width/2 - title.get_width()/2, 5))

        controls = drawInfo.Font.render("Space = Start visualizer, A = Ascending, D = Descending", 1, drawInfo.White)
        drawInfo.window.blit(controls, (drawInfo.width/2 - controls.get_width()/2, 35))

        # updates the information on screen 
        draw_columns.drawList(drawInfo)
        pygame.display.update()

# a class for drawing objects onto the algorithm screen
class draw_columns:
    # function that will update the bars on the screen depending on information sent from the daw_key function
    def drawList(drawInfo, colourPositions={}, clearBG=False):
        array = drawInfo.array

        # only draws the columns without the need to update all elements on the screen
        if clearBG:
            clearRect = (drawInfo.Margin//2, drawInfo.TopBorder,
            drawInfo.width - drawInfo.Margin, drawInfo.height - drawInfo.TopBorder)
            pygame.draw.rect(drawInfo.window, drawInfo.BackgroundColor, clearRect)

        for i, val in enumerate(array):
            # creates different columns based on the size of the window and the value in the algorithm
            x = drawInfo.initializeX + i * drawInfo.DataBlockWidth
            y = drawInfo.height - (val - drawInfo.min) * drawInfo.DataBlockHeight

            # sets the colour of the boxes from the three colour elements assigned
            colour = drawInfo.Gradient[i % 3]

            # sets the colour of the to columns that are being changed
            if i in colourPositions:
                colour = colourPositions[i]

            # drawing all the information determined onto the screen
            pygame.draw.rect(drawInfo.window, colour, (x, y, drawInfo.DataBlockWidth, drawInfo.height))

        if clearBG:
            pygame.display.update()