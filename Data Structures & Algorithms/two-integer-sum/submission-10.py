class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i,num in enumerate(nums):
            s[num] = i
        for j,num in enumerate(nums):
            if target-num in s and s[target-num]!= j:
                return [min(s[target-num],j),max(s[target-num],j)]