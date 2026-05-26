class Solution:
    def rob(self, nums: List[int]) -> int:
        best_from_next_house = 0
        best_from_second_next_house = 0
        if len(nums) == 1:
            return nums[0]


        for i in range(len(nums)-2,-1,-1):
            best_from_current_house = nums[i]+best_from_second_next_house
            skip = best_from_next_house
            best = max(best_from_current_house,skip)
            best_from_second_next_house = best_from_next_house
            best_from_next_house = best
        best1 = best_from_next_house
        best_from_next_house = 0
        best_from_second_next_house = 0
        for i in range(len(nums)-1,0,-1):
            best_from_current_house = nums[i]+best_from_second_next_house
            skip = best_from_next_house
            best = max(best_from_current_house,skip)
            best_from_second_next_house = best_from_next_house
            best_from_next_house = best
        best2 = best_from_next_house
        return max(best1,best2)

        