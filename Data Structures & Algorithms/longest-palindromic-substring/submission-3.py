"""
idea is if a string is a palindrome or has palindromic sides on both front and back, add them to the long_palindrome
then we check all the elements after it and if one of them fucks up, we are done with that palindrome and continue
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>=resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>=resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res

        