"""

we do bfs on the thing

if something is INF, we run bfs

if something is 0, we write the curr distance and push it on to
that position


"""

from collections import deque, defaultdict
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        q = deque()
        nq = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    nq.append((i,j))
        seen = set()
        cell_distance = 0

        while nq:
            q = nq
            nq = deque()
            cell_distance+=1
            while q:
                i,j = q.pop()
                if i-1 >=0 and grid[i-1][j]==INF:
                    nq.appendleft((i-1,j))
                    grid[i-1][j] = cell_distance
                if j-1 >=0 and grid[i][j-1]==INF:
                    nq.appendleft((i,j-1))
                    grid[i][j-1] = cell_distance
                if i+1<len(grid) and grid[i+1][j] == INF:
                    nq.appendleft((i+1,j))
                    grid[i+1][j] = cell_distance
                if j+1<len(grid[i]) and grid[i][j+1]==INF:
                    nq.appendleft((i,j+1))
                    grid[i][j+1] = cell_distance
                
        
            

            

            


                    
                    
                
                
            
            
            


                
                
