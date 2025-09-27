git branch -M main
git push -u origin mainimport pygame
class Cell:

    def __init__(self, xPos, yPos, colour):
       self.size = 100
       self.xPos = xPos
       self.yPos = yPos
       self.colour = colour
       self.occupied = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, [self.xPos, self.yPos, self.size, self.size])