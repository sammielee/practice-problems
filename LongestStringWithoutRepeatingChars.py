"""
Problem:
Given a string s, find the length of the longest substring without repeating characters.

Approach:
current longest substring: longest
check if each subsequent letter is in there
if it is, restart after the first letter location
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 1
        if (len(s) == 0):
            return 0
        longest = s[0]
        leng = 1
        maxLeng = 1
        while i < len(s):
            if s[i] in longest:
                start = longest.index(s[i])
                longest = longest[(start+1):(leng)]
                leng = leng - start
                longest += s[i]
                i += 1
            else:
                longest += s[i]
                leng += 1
                if (leng > maxLeng):
                    maxLeng = leng
                i += 1
                
        return maxLeng
