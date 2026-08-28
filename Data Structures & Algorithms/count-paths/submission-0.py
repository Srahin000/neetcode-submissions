"""
Number of unique paths from the start is 2, left or right

if it is the lowest point or rightest point then there is only one way, either to the right or to down

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        print(dp)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                print(i,j)
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
                
        