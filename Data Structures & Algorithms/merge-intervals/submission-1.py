class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        My plan is to store the first element into curr
        curr = first element
        target = second element

        From the example I'm assuming that it is sorted by first elements

        if curr.last>target.first:
            if curr.last>target.last:
                then nothing changes we just move to the next one
            else:
                curr.last = target.last
        else:
            res.append(curr)
            curr = target

        """
        if len(intervals)==1:
            return intervals
        res = []
        intervals.sort()
        
        curr = intervals[0]
        for i in range(1,len(intervals)):
            target = intervals[i]
            if curr[1]>=target[0]:
                if curr[1]>target[1]:
                    continue
                else:
                    curr[1] = target[1]
            else:
                res.append(curr)
                curr = target
        res.append(curr)
        return res
