class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in range(len(nums)-1,-1,-1):
            temp = max(rob2+nums[i],rob1)
            rob2 = rob1
            rob1 = temp
        return max(rob1,rob2)

            