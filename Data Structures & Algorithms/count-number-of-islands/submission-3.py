class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == "0":
                return
            visited.add((r, c))
            if grid[r][c] == "1":
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    visited.add((r, c))
                elif (r, c) in visited:
                    continue
                else:
                    count += 1
                    dfs(r, c)
        return count
