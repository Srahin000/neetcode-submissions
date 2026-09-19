"""

It would be a dfs with memoize technique, memorizing how many tiles can get to both atlantic and pacific

(0,1)(1,0)(-1,0)(0,-1)

dfs(i,j):
    if i == 0 or j == 0:
        atlantic = True
    else:
        for directions:
            add it to i,j
                if i,j not in seen:
                    if it is a smaller value:
                    atlantic = dfs d+(i,j)
                    if atlantic True break
    if i == len(map)-1 or j== len(map[i])-1:
        pacific = True
    else:
        same thing
    


    return pacific and atlantic

for i
    for j



"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        a = set()
        p = set()
        def pacific(i,j):
            p.add((i,j))
            for d in directions:
                ni=i+d[0]
                nj=j+d[1]
                if ni>=0 and ni<len(heights) and nj>=0 and nj< len(heights[i])and heights[ni][nj]>=heights[i][j] and (ni,nj) not in p:
                    pacific(ni,nj)
        def atlantic(i,j):
            a.add((i,j))
            for d in directions:
                ni=i+d[0]
                nj=j+d[1]
                print(ni,nj)
                if ni>=0 and ni<len(heights) and nj>=0 and nj< len(heights[i]) and heights[ni][nj]>=heights[i][j] and (ni,nj) not in a:
                    atlantic(ni,nj)
                

        for i in range(len(heights)):
            pacific(i,0)
            atlantic(i,len(heights[i])-1)
        for j in range(len(heights[0])):
            pacific(0,j)
            atlantic(len(heights)-1,j)
        res = []

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i,j) in p and (i,j) in a:
                    res.append([i,j])

        return res


            




        