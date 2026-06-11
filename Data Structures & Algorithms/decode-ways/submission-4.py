class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}
        def decode(i):
            if i >=len(s):
                return 1
            if i in mem:
                return mem[i]
            if s[i] == "0":
                return 0
            
            ways = decode(i+1)
            if i<len(s)-1 and int(s[i]+s[i+1])<=26:
                ways += decode(i+2)
            
            mem[i] = ways
            return ways
        
        return decode(0)
            
           