"""
so we need to figure if selling and skipping the day is worth it or holding and selling at a later day is worth it.
 
     1 2 3 4 5
  1 -1 2 3 
  2 0 -3 
  3 
  4 
  5 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {} #(i,buy or sell bool) = profit

        def dp(i,buy):
            if (i,buy) in cache:
                return cache[(i,buy)]
            if i<= len(prices)-2 and buy == False:
                profit= max(-prices[i]+dp(i+1,True),dp(i+1,False))
                cache[(i,buy)] = profit
                return profit
            elif i<= len(prices)-1 and buy == True:
                profit = max( prices[i]+dp(i+2, False), dp(i+1,True))
                cache[(i,buy)] = profit
                return profit
            else:
                return 0
        return dp(0,False)


        
        



            