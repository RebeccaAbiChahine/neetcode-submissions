class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
           return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        island = 0

        def bfs(row, col):
            q = collections.deque([(row, col)])
            visit.add((row, col))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while q:
                currRow, currCol = q.popleft()
            
                for dr, dc in directions:
                    neiRow = currRow + dr
                    neiCol = currCol + dc

                    if 0 <= neiRow < rows and 0 <= neiCol < cols and grid[neiRow][neiCol] == "1" and (neiRow, neiCol) not in visit:
                        visit.add((neiRow, neiCol))
                        q.append((neiRow, neiCol))
                    
                

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    island += 1
                    bfs(row, col)

        return island
    