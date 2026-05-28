class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        mx_height = 0
        while i<j:
            if min(heights[i],heights[j])*(j-i)>mx_height:
                mx_height = min(heights[i],heights[j])*(j-i)
            elif heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return mx_height