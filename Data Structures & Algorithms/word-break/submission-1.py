class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        for each word in dict, we look for match and where it makes us go record the index and the true
        or false values it reaches after exploring that path finishes"

        """
        memo = {}

        def wb(s2,pos):
            print(s2,pos)
            pos1 = pos
            if pos in memo:
                return memo[pos]
            if pos >len(s):
                return False
            if s2 == "" or pos == len(s):
                print("ran")
                return True
            way = False
            for word in wordDict:
                if s2[:len(word)] == word:
                    way = way or wb(s2[len(word):],pos+len(word))
                    memo[pos] = way
            return way

        return wb(s,0)
                    
                
                

                