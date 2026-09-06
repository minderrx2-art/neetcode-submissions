class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_grid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen_rows[r] or board[r][c] in seen_cols[c] or board[r][c] in seen_grid[(r // 3, c // 3)]:
                    return False
                seen_rows[r].add(board[r][c])
                seen_cols[c].add(board[r][c])
                seen_grid[(r // 3, c // 3)].add(board[r][c])
        return True