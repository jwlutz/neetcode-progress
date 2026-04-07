class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        visit = set()
        def dfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == "0"):
                return
            visit.add((r, c))
            dfs(grid, r-1, c, visit)
            dfs(grid, r+1, c, visit)
            dfs(grid, r, c-1, visit)
            dfs(grid, r, c+1, visit)

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if (r, c) in visit:
                    continue
                elif grid[r][c] == "0":
                    continue
                else:
                    self.count += 1
                    dfs(grid, r, c, visit)
        return self.count