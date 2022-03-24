from pygame_visualizer import *

class draw_key:

    def draw(drawInfo, sortingAlgorithmName, ascending):
        drawInfo.window.fill(drawInfo.BackgroundColor)

        title = drawInfo.Font.render(f"{sortingAlgorithmName} - {'Ascending' if ascending else 'Desencding'} ", 1, drawInfo.White)
        drawInfo.window.blit(title, (drawInfo.width/2 - title.get_width()/2, 5))

        controls = drawInfo.Font.render("Key: R = reset, Space = Start visualizer, A = Ascending, D = Descending", 1, drawInfo.White)
        drawInfo.window.blit(controls, (drawInfo.width/2 - controls.get_width()/2, 35))

        draw_columns.drawList(drawInfo)
        pygame.display.update()


class draw_columns:

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