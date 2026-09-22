class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row = len(matrix) - 1
        left_value = 0
        right_value = len(matrix[top_row]) - 1
        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if target <= matrix[middle_row][right_value] and target >= matrix[middle_row][left_value]:
                while left_value <= right_value:
                    middle_value = (left_value + right_value) // 2
                    if target == matrix[middle_row][middle_value]:
                        return True
                    elif target <= matrix[middle_row][middle_value]:
                        right_value = middle_value - 1
                    elif target >= matrix[middle_row][middle_value]:
                        left_value = middle_value + 1
                return False
            elif target <= matrix[middle_row][left_value]:
                bottom_row = middle_row - 1
            elif target >= matrix[middle_row][right_value]:
                top_row = middle_row + 1
        return False