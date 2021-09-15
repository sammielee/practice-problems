"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        if (len(digits) == 0):
            return []
        elif (len(digits) == 1):
            return letters[int(digits)-2]
        else:
            rest = self.letterCombinations(digits[1:])
            ret = []
            for i in rest:
                lets = letters[int(digits[0])-2]
                for j in lets:
                    ret.append(j+i)
        return ret
                
