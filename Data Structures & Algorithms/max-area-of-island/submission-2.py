class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        sizes = [0]
        def helper(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if (row, col) in visited or grid[row][col] == 0:
                    return
                visited.add((row, col))
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                for new_row, new_col in neighbors:
                    helper(new_row, new_col)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 or (row, col) not in visited:
                    before = len(visited)
                    helper(row, col)
                    sizes.append(len(visited) - before)
        return max(sizes)