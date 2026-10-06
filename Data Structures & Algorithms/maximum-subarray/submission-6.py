"""

If it is added and it makes the last sum better, that we add, if not we make the new sum

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = None
        for n in nums:
            if best == None:
                best = n
                m = n
                continue
            best = max(n,best+n)
            
            m = max(m, best)
        m = max(m,best)
        return m
            
                

            
        