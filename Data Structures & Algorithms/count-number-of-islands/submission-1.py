class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            #base case
            
            if grid[r][c] == "0":
                return
            visited.add((r, c))
            #recurse in 4 directions
            directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for dr, dc in directions:
                if 0 <= dr < rows and 0 <= dc < cols and (dr, dc) not in visited:
                    dfs(dr, dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands
                