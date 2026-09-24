PIECES = "PBRQ"


def checkmate(board):
    if not isinstance(board, str):
        print("Error: the board must be a string")
        return

    rows = [line for line in board.splitlines() if line]
    size = len(rows)
    if size == 0:
        print("Error: the board is empty")
        return

    for i, row in enumerate(rows, start=1):
        if len(row) != size:
            print(f"Error: the board must be {size}x{size}, "
                  f"but row {i} has {len(row)} columns")
            return

    