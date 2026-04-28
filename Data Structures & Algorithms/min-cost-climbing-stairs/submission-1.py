class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1 , step2 = cost[-2],cost[-1]

        """
        doing bottom up approach:
        1 cost is cost[-1]
        2 is cost[-2]+cost[-1]
        3 cost is cost[-3]+2cost or cost[-3]+1cost
        4 cost is cost[-4]+3cost
        """

        for i in range(len(cost)-3,-1,-1):
            cost1 = step1+cost[i]
            cost2 = step2+cost[i]
            temp = step1
            step1 = min(cost1,cost2)
            step2 = temp


        return min(step1,step2)
    