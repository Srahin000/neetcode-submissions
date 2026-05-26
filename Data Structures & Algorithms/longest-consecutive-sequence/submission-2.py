class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        max_len = 0
        s=0
        candidates = []
        for i in count:
            if i-1 not in count:
                candidates.append(i)
        for i in candidates:
            j = i
            s= 0
            while j in count:
                s+=1
                j+=1
            max_len = max(s,max_len)
        return max_len
        