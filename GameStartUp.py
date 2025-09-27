import pygame
import sys
import Cell 


pygame.init()
grey = [105,105,105]
screen = pygame.display.set_mode((840, 840))
screen.fill(grey)

pygame.display.update()

def SetupCells():
    cells = [[Cell.Cell(((x * 100) + x * 5), ((y * 100) + y * 5), [255,255,255]) for x in range(8)] for y in range(8)]
    return cells
   
def DrawCells(cells):
   for cell in cells:
        cell.draw(screen)

cells = SetupCells()
DrawCells(cells)
pygame.display.update()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()




    