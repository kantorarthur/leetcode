def dfs(grid: List[List[int]], row: int, col: int) -> int:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        return 0
    fish = grid[row][col]
    grid[row][col] = 0
    return fish + dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col - 1)

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        max_fish = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                cur_fish = 0
                if grid[row][col] != 0:
                    cur_fish = dfs(grid, row, col)
                    if cur_fish > max_fish:
                        max_fish = cur_fish
        return max_fish
        