""" 

Input: s = "III"
Output: 3
Explanation: III = 3. 

create an object for each roman value in intejer 
fore every roman number if the next number is bigger 
"""


class Solution(object):
    def romanToInt(s):
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace(
            "XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
            
        print(sum(map(lambda x: roman_to_integer[x], s)))


Solution.romanToInt("MCMXCIV")
