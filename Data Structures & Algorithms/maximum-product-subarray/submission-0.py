class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = []
        temp = set()
        for i in range(len(nums)-1,-1,-1):
            arr.append(1)
            for j in range(len(arr)):
                arr[j] = arr[j]*nums[i]
            temp.add(max(arr))
        temp.add(max(nums))
        return max(temp)
                