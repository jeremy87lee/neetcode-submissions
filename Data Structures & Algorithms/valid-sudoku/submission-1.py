class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxMap = defaultdict(list)
        colMap = defaultdict(list)
        for j,row in enumerate(board):
            rowSet = set()
            for i in range(len(row)):
                if row[i] in rowSet and row[i] != '.':
                    return False
                rowSet.add(row[i])
                if row[i] in colMap[i] and row[i] != '.':
                    return False
                colMap[i].append(row[i])
                if row[i] in boxMap[i//3,j//3] and row[i] != '.':
                    return False
                boxMap[i//3,j//3].append(row[i])
        return True