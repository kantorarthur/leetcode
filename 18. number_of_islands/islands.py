def dfs(grid: List[List[str]], row: int, col: int) -> None:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
        return
    grid[row][col] = '0'
    dfs(grid, row + 1, col)
    dfs(grid, row - 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row, col - 1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        number_of_islands = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0]) ):
                if grid[row][col] == '1':
                    number_of_islands += 1
                    dfs(grid, row, col)
        
        return number_of_islands