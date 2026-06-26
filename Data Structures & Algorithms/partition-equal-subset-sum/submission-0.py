"""

[1,2,3,4]
[1]
[]
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def trav(s, rest):
            if not rest:
                return False
            if s == sum(rest):
                return True
            if (s,tuple(rest)) in memo:
                return True
            res = False
            for i in range(len(rest)):
                res = trav(s+rest[i], rest[:i]+rest[i+1:])
                if res == True:
                    memo[(s,tuple(rest))] = True
                    return res
            return res
        
        return trav(0,nums)
                
            

            


