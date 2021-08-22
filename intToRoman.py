"""
Given an integer, convert it to a roman numeral.
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        if num >= 1000:
            thousand = num//1000
            i = 0
            while i < thousand:
                ret += 'M'
                i+=1
            num = num - thousand*1000
        if num >= 500:
            hundred = num//100
            i = 0
            if hundred == 9:
                ret += "CM"
            elif hundred == 5:
                ret += "D"
            else:
                ret += "D"
                while i < hundred-5:
                    ret += "C"
                    i += 1
            num = num - hundred*100
        if num >= 100:
            hundred = num//100
            i = 0
            if hundred == 4:
                ret += "CD"
            else:
                while i < hundred:
                    ret += "C"
                    i += 1
            num = num - hundred*100
        if num >= 50:
            ten = num//10
            i = 0
            if ten == 9:
                ret += "XC"
            elif ten == 5:
                ret += "L"
            else:
                ret += "L"
                while i < ten-5:
                    ret += "X"
                    i += 1
            num = num - ten*10
        if num >= 10:
            ten = num//10
            i = 0
            if ten == 4:
                ret += "XL"
            else:
                while i < ten:
                    ret += "X"
                    i += 1
            num = num - ten*10
        if num >= 5:
            i = 0
            if num == 9:
                ret += "IX"
            elif num == 5:
                ret += "V"
            else:
                ret += "V"
                while i < num - 5:
                    ret += "I"
                    i += 1
            return ret
        if num >= 1:
            i = 0
            if num == 4:
                ret += "IV"
            else:
                while i < num:
                    ret += "I"
                    i += 1
        return ret
                
                
        
