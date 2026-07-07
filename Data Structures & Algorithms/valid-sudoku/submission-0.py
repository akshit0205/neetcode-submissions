class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowd=defaultdict(set)
        columnd=defaultdict(set)
        boxes=defaultdict(set)
        for row in range(9):
            for col in range(9):
                x=board[row][col]
                if x == ".":
                    continue
                if x in rowd[row] or x in columnd[col] or x in boxes[(row//3),(col//3)]:
                    return False
                rowd[row].add(x)
                columnd[col].add(x)
                boxes[(row // 3, col // 3)].add(x)
        return True 