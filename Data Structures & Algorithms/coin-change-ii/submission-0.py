"""
  _ 1 2 3
_ 4 3 
1 3 2
2 2 1
3 1 0

so at each coin, we can take it, take it again or move to the next coin
if our reach goes over the target, then we start going back



"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        output = 0
        memo = {}

        def chng(i,rem):
            if (i,rem) in memo:
                return memo[(i,rem)]
            if i>=len(coins):
                return 0
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            r = chng(i,rem-coins[i]) + chng(i+1,rem)
            memo[(i,rem)] = r
            return r
        return chng(0,amount)


            

            