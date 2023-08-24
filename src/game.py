import pygame
from const import *
from board import Board
from dragger import Dragger
from config import Config
class Game:
    def __init__(self):
        self.next_player = 'white'
        self.hoverd_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    # show method
    def show_bg(self, surface): 
        theme = self.config.theme
        for  row in  range(ROWS):
            for col in range(COLS):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) #light green
                else:
                    color = (119, 154, 88) # Dark Green
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    # show pieces method 
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # pieces ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    # all piece expect dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture) 
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
    def show_moves(self, surface):
        theme = self.config.theme
        if self.dragger.dragging:
            piece = self.dragger.piece
            # loop all valid move
            for move in piece.moves:
                # color
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                #if move.final.row + move.final.col % 2 == 0:
                 #   color = "#C86464"
                #else:
                 #   "#C84646"
                # rect 
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect) 
    def show_last_move(self, surface):
        theme = self.config.theme
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark 
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
    def show_hover(self, surface):
        if self.hoverd_sqr:
             # color
                color = (180, 180, 180)
                # rect
                rect = (self.hoverd_sqr.col * SQSIZE, self.hoverd_sqr.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect, width=3)

    # other method
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, col):
        self.hoverd_sqr = self.board.squares[row][col]
    def change_theme(self):
        self.config.change_theme()