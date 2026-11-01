class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        island = 0
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = collections.deque([(r, c)])

            while q:
                cr, cc = q.popleft()
                directions = [[-1 , 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        bfs(nr, nc)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    bfs(i, j)
        
        return island