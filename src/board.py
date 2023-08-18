from const import * 
from square import Square
from piece import *
from move import Move
class Board:
    def __init__(self):
       self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for  col in range(COLS)]
       self.last_move = None
       self._create()
       self.__add_pieces("white")
       self.__add_pieces("black")

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # console board move update 
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # move 
        piece.moved = True
        # clear valid move
        piece.clear_moves()
        # set last move
        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.moves

     
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
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir): 
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # create initial and final squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
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
                            
                            #final_piece = self.squares[possible_move_row][possible_move_col].piece
                            # create new move
                            move = Move(initial, final)

                            # new move 
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
                (row-2, col-1), 
                ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # create new move
                        initial = Square(row, col)
                        #final_piece = self.squares[possible_move_row][possible_move_col].piece
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_move(move) 
                    
                    
        def straightline_moves(incrs):
        
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr
                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                    # create squares of new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                    # create possible new move
                        move = Move(initial, final)

                    # empty = continue looping
                        if self.squares[possible_move_row][possible_move_col].isempty():
                        # append new move
                            piece.add_move(move)
                    # has enemy piece
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            piece.add_move(move)
                            break
                     # team piece = break
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break  
                    # not in range
                    else:
                        break
                    # increamenting incrs
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr
        def king_moves():
            adj = [
                (row-1, col+0), # up
                (row-1, col+1), # upght
                (row+0, col+1), # right
                (row+1, col+1), # down-right
                (row+1, col+0), # down
                (row+1, col-1), # down-left
                (row+0, col-1), # left
                (row-1, col-1), # up-left
            ]
            # normal move
            for possible_move in adj:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color): 
                         # create new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece
                        move = Move(initial, final)
                        # append new valid move
                        piece.add_move(move) 
            # castling moves

            # queen castling
            # king castling

        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1, 1), # up right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                ])
        elif isinstance(piece, Rook):
            straightline_moves([
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left
                ]) 
        elif isinstance(piece, Queen):
            straightline_moves([
                (-1, 1), # up right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (-1, 0), # up
                (0, 1), # right
                (1, 0), # down
                (0, -1), # left

            ])
        elif isinstance(piece, King):
            king_moves()


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
      
      
      