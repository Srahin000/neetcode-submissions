class Solution:
    def numDecodings(self, s: str) -> int:
        mem = {}
        def decode(i):
            if i in mem:
                return mem[i]
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            ways = decode(i+1)
            if i+1 <len(s):
                two_digit = int(s[i:i+2])
                if 10 <= two_digit <=26:
                    ways += decode(i+2)
            mem[i] = ways
            return ways
        return decode(0)