class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            s = set()
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    print(i, j)
                    return False
                else:
                    s.add(board[i][j])
        for j in range(0, 9):
            s = set()
            for i in range(0, 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        i = 0
        j = 0
        while i < 9 and j < 9:
            print(i, j)
            s = set()
            for a in range(i, i + 3):
                for b in range(j, j + 3):
                    if board[a][b] == ".":
                        continue
                    elif board[a][b] in s:
                        return False
                    else:
                        s.add(board[a][b])
            j += 3
            if j > 6:
                j = 0
                i += 3

        return True