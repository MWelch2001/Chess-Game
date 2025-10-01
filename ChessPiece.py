import pygame

class ChessPiece:
    def __init__(self, team, type, location, image, killable=False):
        self.team = team
        self.type = type
        self.location = location
        self.image = pygame.image.load(image)
        self.killable = killable
        