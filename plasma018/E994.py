class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        queue = list()
        fresh = 0
        minutes = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
    
        while len(queue) != 0:
            minutes += 1
            size = len(queue)
            while size != 0:
                size -= 1
                (i,j) = queue.pop(0)
                
                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    queue.append((i-1, j))
                    fresh -= 1
                if i < row-1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    queue.append((i+1, j))
                    fresh -= 1
                if j > 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    queue.append((i, j-1))
                    fresh -= 1
                if j < column-1 and grid[i][j+1] == 1: 
                    grid[i][j+1] = 2
                    queue.append((i, j+1))
                    fresh -= 1
         
        return max(minutes-1,0) if fresh is 0 else -1
