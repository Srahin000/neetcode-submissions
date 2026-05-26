class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums)>2:
            nums[-3] = nums[-3]+nums[-1]
        for i in range(len(nums)-4,-1,-1):
            nums[i] = max(nums[i]+nums[i+2],nums[i]+nums[i+3])
        return max(nums[0],nums[1])
        """


        rob1,rob2 = 0,0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return max(rob1,rob2)

            