class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box(boxid,board):
            square=[]
            for r in range(boxid[0],boxid[0]+3):
                for c in range(boxid[1],boxid[1]+3):
                    square.append(board[r][c])
            return square
        
        def check(row):
            seen = set()
            for char in row:
                if char != '.':
                    if char in seen:
                        return False
                    seen.add(char)
            return True

        lines=board
        column=[]
        for i in range(len(board)):
            col=[]
            for j in range (len(board[i])):
                col.append(board[j][i])
            column.append(col)
        boxid=[]
        for i in range(3):
            for j in range((3)):
                boxid.append([i*3,j*3])
        squares=[]
        for i in boxid:
            squares.append(box(i,board))
        for i in squares:
            if check(i):
                continue
            else:
                return False
        for i in lines:
            if check(i):
                continue
            else:
                return False
        for i in column:
            if check(i):
                continue
            else:
                return False
        return True

    
        