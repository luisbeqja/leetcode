""" 
PROBLEM:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

EXAMPLES:
    Input: s = "()[]{}"
    Output: true

SOLUTION:
    get a string of brackets
    check if the string is empty
    if not empty ckeck the first brucket an and set it in Time variable
    doit for the lent of the string

"""


class Solution(object):
    def isValid(self, s):
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0


if __name__ == "__main__":
    s = "()[{}"
    print(Solution().isValid(s))
