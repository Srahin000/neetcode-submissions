class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        we start with c, and then it is a palindrome, add to the answers
        and then we take b and add it to the palindrome of the one before and then we take a and add it to the palindrome before
        
        then we start with b and add it to the palindrome and then go back and add a to all the palindromes
        """
        res = []

        for i in range(0,len(s)):
            l = i-1
            r = i+1
            sub = s[i]
            res.append(sub)
            while l>-1 and r<len(s) and s[l]==s[r]:
                sub = s[l]+sub+s[r]
                l-=1
                r+=1
                res.append(sub)
        for i in range(1,len(s)):
            l = i-1
            r = i
            if s[l]!=s[r]:
                continue
            sub = s[l]+s[r]
            res.append(sub)
            l-=1
            r+=1
            
            while l>-1 and r<len(s) and s[l]==s[r]:
                sub = s[l]+sub+s[r]
                l-=1
                r+=1
                res.append(sub)
        
        return len(res)
            
                
            


                


