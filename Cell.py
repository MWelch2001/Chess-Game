import pygame

class Cell:

    def __init__(self, xPos, yPos):
       self.size = 100
       self.xPos = xPos
       self.yPos = yPos
       self.occupied = False

    def draw(self, screen, colour):
        
        pygame.draw.rect(screen, colour, [((self.xPos * 100) + self.xPos * 5 + 5), ((self.yPos * 100) + self.yPos * 5 + 5), self.size, self.size])