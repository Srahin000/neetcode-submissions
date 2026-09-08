"""
text1 = cat
text2 = crabt

at 1, if the texts matches then we have a match and longest sequence is c
at 2, we have a and 


  -cat
-  000
c  111
r  011
a  000
b  011
t  011
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2)+1)] for _ in range(len(text1)+1)]
        #[[][][]]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp)
        return dp[-1][-1]

            

        