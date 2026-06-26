class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def trav(prev,pos):
            if pos >= len(nums):
                return 0
            if (prev,pos) in memo:
                return memo[(prev,pos)]
            res = trav(prev,pos+1)
            if nums[pos]>prev:
                res = max(res,1+trav(nums[pos],pos+1))
            memo[(prev,pos)] = res
            return res
        return trav(-float('inf'),0)