class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            j = 0
            tracker = []
            while j < len(i):
                if i[j] not in tracker:
                    tracker.append(i[j])
                elif i[j] != ".":
                    return False
                j += 1
        k = 0
        while k < len(board):
            tracker2 = []
            for i in board:
                if i[k] not in tracker2:
                    tracker2.append(i[k])
                elif i[k] != ".":
                    return False
            k += 1
        board1 = board[0:3]
        board2 = board[3:6]
        board3 = board[6:9]
        for row_group in [board1, board2, board3]:
            for start in [0, 3, 6]:
                temp_list = []

                for row in row_group:
                    for col in range(start, start + 3):
                        cell = row[col]

                        if cell not in temp_list:
                            temp_list.append(cell)
                        elif cell != ".":
                            return False

        return True