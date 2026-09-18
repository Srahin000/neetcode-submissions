from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nq = deque()
        dirs = [(0,1),
        (1,0),
        (0,-1),
        (-1,0)
        ]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    nq.append((i,j))
        res_min = 0

        while nq:
            q = nq
            nq = deque()
            while q:
                c = q.popleft()
                for d in dirs:
                    i,j = c
                    a, b = d
                    i +=a
                    j+=b
                    if i>=0 and i<(len(grid)) and j>=0 and j<len(grid[i]):
                        if grid[i][j] == 1:
                            nq.append((i,j))
                            grid[i][j] = 2
            if nq:
                res_min+=1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return res_min
            
