class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colMap = defaultdict(list)
        rowSet = set()
        boxMap = defaultdict(list)

        for index_row,row in enumerate(board):
            rowSet = set()
            for index_col,num in enumerate(row):
                if num in rowSet and num != '.':
                    print("ROW ERROR")
                    return False
                elif num != '.':
                    rowSet.add(num)

                if num in colMap[index_col] and num != '.':
                    print("COLUMN ERROR")
                    return False
                elif num != '.': 
                    colMap[index_col].append(num)

                if num in boxMap[index_row//3,index_col//3] and num != '.':
                    print("BOX ERROR")
                    return False
                elif num != '.':
                    boxMap[index_row//3,index_col//3].append(num)
        return True