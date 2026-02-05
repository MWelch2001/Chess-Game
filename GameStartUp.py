import pygame
import sys
import Cell 
import Piece


pygame.init()
grey = [105,105,105]
white = [255,255,255]
screenSize = 590
cellAmount = 9
cellBorder = 5
screen = pygame.display.set_mode((screenSize, screenSize))
screen.fill(grey)

def LoadWhitePieces():
   whitePieces = [Piece.Piece('w', 'p', [x, 6], 60, cellBorder) for x in range(9)] 
   return whitePieces

def SetupCells():
    cells = [[Cell.Cell(screenSize - (cellBorder * (cellAmount + 1)), cellAmount, cellBorder, x, y) for x in range(9)] for y in range(9)]
    return cells
   
def DrawCells(cells):
   for x in range (9):
       for y in range(9):   
            cells[x][y].draw(screen, white)


cells = SetupCells()
DrawCells(cells)

whitePieces = LoadWhitePieces()
for whitePiece in whitePieces:
   whitePiece.draw(screen)
pygame.display.update()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()




    