class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul= 1
        new_num = []
        new_num2= []
        for i in nums:
            new_num.append(prefix_mul)
            prefix_mul*=i
        prefix_mul =1
        for i in reversed(nums):
            new_num2.append(prefix_mul)
            prefix_mul*=i
        new_num2 = list(reversed(new_num2))

        for i in range(len(new_num)):
            new_num[i]*=new_num2[i]
        return new_num
        


            