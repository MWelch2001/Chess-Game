import pygame
import sys
import Cell 
import ChessPiece


pygame.init()
grey = [105,105,105]
white = [255,255,255]
beige = [207,185,151]
screen = pygame.display.set_mode((845, 845))
screen.fill(grey)

def LoadWhitePieces():
   whitePieces = [ChessPiece.ChessPiece('w', 'p', [x, 6], "Resources/WP.png") for x in range(8)] 
   return whitePieces

def SetupCells():
    cells = [[Cell.Cell(x, y) for x in range(8)] for y in range(8)]
    return cells
   
def DrawCells(cells):
   colourCounter = 0
   for x in range (8):
       for y in range(8):   
           if colourCounter % 2 == 0:
            cells[x][y].draw(screen, white)
           else:
            cells[x][y].draw(screen, beige)
           colourCounter += 1
       colourCounter += 1

cells = SetupCells()
DrawCells(cells)
whitePieces = LoadWhitePieces()
for whitePiece in whitePieces:
   screen.blit(whitePiece.image, (((whitePiece.location[0] * 100) + whitePiece.location[0] * 5 + 22.5),((whitePiece.location[1] * 100) + whitePiece.location[1] * 5 + 22.5)))
pygame.display.update()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()




    