class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        counter = 0
        def helper(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if (row, col) in visited or grid[row][col] == '0':
                    return
                visited.add((row, col))
                helper(row + 1, col)
                helper(row - 1, col)
                helper(row, col + 1)
                helper(row, col - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    counter += 1
                    helper(i, j)
        return counter