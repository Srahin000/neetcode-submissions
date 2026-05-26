class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # 1. Define the logic once
        def rob_simple(start_index: int, end_index: int) -> int:
            best_from_next_house = 0
            best_from_second_next_house = 0
            
            # Loop runs backward between the boundaries provided
            for i in range(end_index, start_index - 1, -1):
                best_from_current_house = nums[i] + best_from_second_next_house
                skip = best_from_next_house
                
                best = max(best_from_current_house, skip)
                
                best_from_second_next_house = best_from_next_house
                best_from_next_house = best
                
            return best_from_next_house

        # 2. Call the logic twice for your two timelines
        
        # Timeline 1: Skip the LAST house
        best1 = rob_simple(0, len(nums) - 2)
        
        # Timeline 2: Skip the FIRST house
        best2 = rob_simple(1, len(nums) - 1)
        
        # 3. Return the maximum of the two timelines
        return max(best1, best2)