class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        def change(amount):
            if amount == 0:
                return 0
            if amount < 1:
                return float("inf")
            best = float("inf")
            if amount in mem:
                return mem[amount]
            for coin in coins:
                best = min(best, 1+change(amount-coin))
                mem[amount] = best
            
            return best
        res = change(amount)
        if res == float("inf"):
            return -1
        return res
        

            
        