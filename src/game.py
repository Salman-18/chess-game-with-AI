import pygame
from const import *
from board import board
class Game:
    def __init__(self):
        self.board = board()
    # show method
    def show_bg(self, surface):
        for  row in  range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) # Dark Green
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # pieces ?
                if self.board.sqaure[row][col].has_pieces():
                    piece = self.board.square[row][col].piece
                    img = pygame.image.load(piece.texture) 
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_react = img.get.rect(center = img_center)
                    surface.blit(img, piece.texture_react)


