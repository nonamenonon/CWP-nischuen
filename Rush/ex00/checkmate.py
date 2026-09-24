PIECES = "PBRQ"
KING = "K"

def checkmate(board):
    if not isinstance(board, str):
        print("Fail")
        return

    rows = [line for line in board.splitlines() if line]
    size = len(rows)
    if size == 0:
        return

    for row in rows:
        if len(row) != size:
            return
        
    king_position = [
        (r, c)
        for r, row in enumerate(rows)
        for c, ch in enumerate(row)
        if ch == KING
    ]
    if len(king_position) != 1:
        return
    king_pos = king_position[0]

    if is_in_check(rows, king_pos):
        print("Success")
    else:
        print("Fail")

def in_bounds(r, c, size):
    return 0 <= r < size and 0 <= c < size

def is_blocking(ch):
    return ch in PIECES or ch == KING

def pawn_attacks(piece_pos, king_pos):
    pr, pc = piece_pos
    return king_pos in [(pr - 1, pc - 1), (pr - 1, pc + 1)]

def slides_to_king(piece_pos, king_pos, directions, grid):
    size = len(grid)
    pr, pc = piece_pos
    for dr, dc in directions:
        r, c = pr + dr, pc + dc
        while in_bounds(r, c, size):
            if (r, c) == king_pos:
                return True
            if is_blocking(grid[r][c]):
                break
            r += dr
            c += dc
    return False

BISHOP_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
ROOK_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
QUEEN_DIRS = BISHOP_DIRS + ROOK_DIRS

def piece_attacks_king(piece, piece_pos, king_pos, grid):
    if piece == "P":
        return pawn_attacks(piece_pos, king_pos)
    if piece == "B":
        return slides_to_king(piece_pos, king_pos, BISHOP_DIRS, grid)
    if piece == "R":
        return slides_to_king(piece_pos, king_pos, ROOK_DIRS, grid)
    if piece == "Q":
        return slides_to_king(piece_pos, king_pos, QUEEN_DIRS, grid)
    return False

def is_in_check(grid, king_pos):
    size = len(grid)
    for r in range(size):
        for c in range(size):
            ch = grid[r][c]
            if ch in PIECES:
                if piece_attacks_king(ch, (r, c), king_pos, grid):
                    return True
    return False