"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""
"""
Approach
if num of rows is 1, return s
row increments which row you're on and what index you start on
curr is current letter you are on

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        row = 0
        curr = 0 
        ret = ""
        incr = (numRows - 1)*2
        while (row < numRows):
         
            if (curr >= len(s)):
                row += 1
                curr = row
                if (row == numRows-1):
                    incr = (numRows - 1)*2
                elif (numRows%2 == 1 and row == numRows//2):
                    incr = numRows-1
                else:
                    incr = (numRows - row - 1) *2
            else:
                ret += s[curr]
                curr += incr
                if (row != 0 and row != numRows-1 and (numRows%2 != 1 or row != numRows//2)):
                    
                    if (incr != (numRows - (numRows - 1 - row) - 1) *2):
                        incr = (numRows - (numRows - 1 - row) - 1) *2
                    else:
                        incr = (numRows - row - 1) *2
        return ret
