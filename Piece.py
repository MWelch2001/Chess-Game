from turtle import left
import pygame

class Piece:
    def __init__(self, team, type, location, cellSize,  cellBorder):
        self.team = team
        self.type = type
        self.location = location
        self.cellSize = cellSize
        self.cellBorder = cellBorder
        self.isPromoted = False
        self.can_promote = self.type not in ['K', 'G']
        # Intermediate font size between previous and current settings
        self.font = pygame.font.SysFont("Arial", max(8, int(cellSize * 0.31)), bold=True)

        
    def promote(self):
        """Attempts to promote the piece if eligible."""
        if self.can_promote and not self.is_promoted:
            self.is_promoted = True
            
            promotion_map = {
                'P': 'P+', 'L': 'L+', 'N': 'N+', 
                'S': 'S+', 'R': 'R+', 'B': 'B+'
            }
            self.type = promotion_map.get(self.type, self.type)
            return True
        return False
    
    def draw(self, surface):
        # Extra internal padding so the piece doesn't touch the border (scales)
        basePadding = max(2, int(self.cellSize * 0.06))
        # Intermediate shrink (between prior small and aggressive shrink)
        shrinkAmount = max(1, int(self.cellSize * 0.09))

        # Compute the cell's top-left using the same formula as Cell.draw:
        # cell_left = x * size + (x+1) * cellBorder
        # Use rounding to match how pygame ultimately rasterizes positions
        cellLeftBound = round(self.location[0] * self.cellSize + (self.location[0] + 1) * self.cellBorder)
        cellTopBound = round(self.location[1] * self.cellSize + (self.location[1] + 1) * self.cellBorder)

        # Boundaries of the piece within the inset cell, with extra shrink
        L = cellLeftBound + basePadding + shrinkAmount
        R = cellLeftBound + round(self.cellSize) - basePadding - shrinkAmount
        T = cellTopBound + basePadding + shrinkAmount
        B = cellTopBound + round(self.cellSize) - basePadding - shrinkAmount
        
        # True center within the inset (accounts for border + internal padding)
        xMid = round((L + R) / 2)
        yMid = round((T + B) / 2)
        # Small vertical offset for text placement that scales with cell size
        offsetAmount = max(1, round(self.cellSize * 0.05))

        # Slight inset for the tip so the whole polygon doesn't touch the cell edge
        polygonTipInset = max(1, int((B - T) * 0.06))

        # Shoulder drop (how far down the 'slant' starts)
        shoulderOffset = round((B - T) / 3)

        if self.team == 'black': # Points UP
            points = [
                (xMid, T + polygonTipInset),      # Tip (Top Center, inset)
                (R, T + shoulderOffset),         # Right Shoulder
                (R, B),                      # Bottom Right
                (L, B),                      # Bottom Left
                (L, T + shoulderOffset)          # Left Shoulder
            ]
            # Text is shifted down slightly to sit in the 'belly' of the piece
            text_pos = (xMid, yMid + offsetAmount)
        else: # White: Points DOWN
            points = [
                (xMid, B - polygonTipInset),      # Tip (Bottom Center, inset)
                (L, B - shoulderOffset),         # Left Shoulder
                (L, T),                      # Top Left
                (R, T),                      # Top Right
                (R, B - shoulderOffset)          # Right Shoulder
            ]
            # Text is shifted up slightly to sit in the 'belly' of the piece
            text_pos = (xMid, yMid - offsetAmount)

        # 1. DRAW BODY
        pygame.draw.polygon(surface, (245, 222, 179), points) # Wood color
        pygame.draw.polygon(surface, (0, 0, 0), points, 2)    # Outline

        # 2. DRAW TEXT
        color = (200, 0, 0) if self.isPromoted else (0, 0, 0)
        text_surf = self.font.render(self.type, True, color)
        
        if self.team == 'white':
            text_surf = pygame.transform.rotate(text_surf, 180)

        # 3. ALIGNMENT
        # Ensure integer pixel positions for blitting to avoid subpixel rounding
        text_rect = text_surf.get_rect(center=(int(round(text_pos[0])), int(round(text_pos[1]))))
        surface.blit(text_surf, text_rect)