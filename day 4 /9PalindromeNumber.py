"""  
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

EXAMPLES:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

SOLUTION:
    get an integer and trasform it in a string
    check if the string is empty or one char
    create a reverse string of the input string
    compare the two strings
    if they are the same return true
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x) == 0 or len(x) == 1:
            return True
        else:
            x_reverse = x[::-1]
            if x == x_reverse:
                print(x)
                return True
            else:
                return False
        
