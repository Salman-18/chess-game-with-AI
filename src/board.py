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
        calculate all possible (valid) moves of an specific on specific postion
        """
        def pawn_moves():
            # steps
            steps = 1 if piece.moved else 2
            #if piece.moved:
             #   steps = 1
            #else:
             #   steps = 2
             # vertical Move
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps ))
            for move_row in range(start, end, piece.dir): 
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        # create initial and final squares
                        initial = Square(row, col)
                        final = Square(move_row, col)
                         # create new move
                        move = Move(initial, final)
                        # append new move
                        piece.add_move(move)
                    # blocked
                    else:
                        break
                  # not in range
                else: 
                    break    
                # Diagonal moves
                possible_move_row = row + piece.dir
                possible_move_cols = [col-1, col+1]
                for possible_move_col in possible_move_cols:
                    if Square.in_range(possible_move_row, possible_move_col):
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            # create initial and final squares
                            initial = Square(row, col)
                            final = Square(possible_move_row, possible_move_col)
                            # create a new move
                            move = Move(initial, final)
                            # append new move 
                            piece.add_move(move)
                            
                            
                            
                            
        def knight_moves():
           
          # 8 possible move 
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
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # create new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_move(move)
                    # blocked
                    else:
                        break
                # not in range
                else:
                    break
        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr
                #while True
                if Square.in_range(possible_move_row, possible_move_col):
                  # empty
                  if self.squares[possible_move_row][possible_move_col].isempty():
                      pass
                  # has enemy piece
                  if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                      pass

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1,1), # up right
                (-1,-1), # up-left
                (1,1), # down-right
                (1,-1) # down-left
                ])
        elif isinstance(piece, Rook):
            straightline_moves([
                (-1,0), # up
                (0,1), # left
                (1,0), # down
                (0,-1) # right
                ])
        elif isinstance(piece, Queen):
            straightline_moves([
                (-1,1), # up right
                (-1,-1), # up-left
                (1,1), # down-right
                (1,-1), # down-left
                (-1,0), # up
                (0,1), # left
                (1,0), # down
                (0,-1) # right

            ])
        elif isinstance(piece, King):
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
          self.squares[5][1] = Square(5, 1, Pawn(color))
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