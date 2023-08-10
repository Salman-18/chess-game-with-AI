from const import * 
from square import Square
from piece import *
from move import Move
class Board:
    def __init__(self):
       self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for  col in range(COLS)]
       self._create()
       self.__add_pieces("white")
       self.__add_pieces("black")
     
    def calc_moves(self, piece, row, col):
        """
        calculate all possible (valid) moves of an specific an specific postion
        """
        def Knight_moves():
            # 8 possible moves
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1)]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # create new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_move(move)

        if isinstance(Piece, Pawn):
            pass 
        elif isinstance(Piece, Knight):
            pass 
        elif isinstance(Piece, Bishop):
            pass 
        elif isinstance(Piece, Rook):
            pass 
        elif isinstance(Piece, Queen):
            pass 
        elif isinstance(Piece, King):
            pass 


    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def __add_pieces(self, color):
      row_pawn, row_other = (6, 7) if color == "white" else (1, 0)
      #pawn
      for col in range(COLS):
          self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
    #Knight 
      self.squares[row_other][1] = Square(row_other, 1, Knight(color))
      self.squares[row_other][6] = Square(row_other, 6, Knight(color))
    #bishop 
      self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
      self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
    #rook 
      self.squares[row_other][0] = Square(row_other, 0, Rook(color))
      self.squares[row_other][7] = Square(row_other, 7, Rook(color))
    #Queen
      self.squares[row_other][3] = Square(row_other, 3, Queen(color))
    #King 
      self.squares[row_other][4] = Square(row_other, 4, King(color))