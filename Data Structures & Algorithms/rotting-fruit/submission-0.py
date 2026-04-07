from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_count -= 1
            minutes += 1
        return minutes if fresh_count == 0 else -1