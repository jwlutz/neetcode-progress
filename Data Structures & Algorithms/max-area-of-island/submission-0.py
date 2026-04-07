class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_size = 0
        visited = set()

        def dfs(grid, r, c, visited):
            rows, cols = len(grid), len(grid[0])
            total = 1
            if (min(r, c) < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == 0):
                return 0
            visited.add((r, c))
            
            total += dfs(grid, r-1, c, visited)
            total += dfs(grid, r+1, c, visited)
            total += dfs(grid, r, c-1, visited)
            total += dfs(grid, r, c+1, visited)
            if total > self.max_size:
                self.max_size = total
            return total


        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    continue
                elif (r, c) in visited:
                    continue
                else:
                    dfs(grid, r, c, visited)

        return self.max_size


