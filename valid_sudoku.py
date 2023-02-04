def valid_sudoku(board):
    N = 9
    rows = [set() for _ in range(N)]
    columns = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    print(rows)
    print(columns)
    print(boxes)

    for r in range(N):
        for c in range(N):
            val = board[r][c]
            if val == ".":
                continue
            
            if val in rows[r]:
                return False
            rows[r].add(val)
            print(rows[r])

            if val in columns[c]:
                return False
            columns[c].add(val)
            print(columns[c])

            idx = (r//3) * 3 + c//3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)
            print(boxes[idx])

    return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

    print(valid_sudoku(board))
