import pygame

class Cell:

    def __init__(self, screenSize, cellAmount, cellBorder, xPos, yPos):
       self.size = screenSize / cellAmount
       self.cellBorder = cellBorder
       self.xPos = xPos
       self.yPos = yPos
       self.occupied = False

    def draw(self, screen, colour):
        
        pygame.draw.rect(screen, colour, [((self.xPos * self.size) + self.xPos * 5 + 5), ((self.yPos * self.size) + self.yPos * 5 + 5), self.size, self.size])