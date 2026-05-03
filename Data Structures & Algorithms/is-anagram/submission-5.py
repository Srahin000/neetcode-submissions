class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = collections.Counter(s)
        countt = collections.Counter(t)
        return counts==countt