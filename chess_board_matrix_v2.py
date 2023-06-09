queen = "queen"
king = "king"
bishop = "bishop"
knight = "knight"
rook = "rook"
pawn = "pawn"
empty = "_"
board = []

for i in range(8):
    row = [empty for i in range(8)]
    board.append(row)

board[0][0] = rook
board[0][1] = knight
board[0][2] = bishop
board[0][3] = king
board[0][4] = queen
board[0][5] = bishop
board[0][6] = knight
board[0][7] = rook
board[1][0] = pawn
board[1][1] = pawn
board[1][2] = pawn
board[1][3] = pawn
board[1][4] = pawn
board[1][5] = pawn
board[1][6] = pawn
board[1][7] = pawn
board[2][0] = empty
board[2][1] = empty
board[2][2] = empty
board[2][3] = empty
board[2][4] = empty
board[2][5] = empty
board[2][6] = empty
board[2][7] = empty
board[3][0] = empty
board[3][1] = empty
board[3][2] = empty
board[3][3] = empty
board[3][4] = empty
board[3][5] = empty
board[3][6] = empty
board[3][7] = empty
board[4][0] = empty
board[4][1] = empty
board[4][2] = empty
board[4][3] = empty
board[4][4] = empty
board[4][5] = empty
board[4][6] = empty
board[4][7] = empty
board[5][0] = empty
board[5][1] = empty
board[5][2] = empty
board[5][3] = empty
board[5][4] = empty
board[5][5] = empty
board[5][6] = empty
board[5][7] = empty
board[6][0] = pawn
board[6][1] = pawn
board[6][2] = pawn
board[6][3] = pawn
board[6][4] = pawn
board[6][5] = pawn
board[6][6] = pawn
board[6][7] = pawn
board[7][0] = rook
board[7][1] = knight
board[7][2] = bishop
board[7][3] = king
board[7][4] = queen
board[7][5] = bishop
board[7][6] = knight
board[7][7] = rook

print(f"{board[0]} \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]} \n{board[5]} \n{board[6]} \n{board[7]}")


