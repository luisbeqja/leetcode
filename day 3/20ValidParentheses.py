class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        return ('()' in s or '{}' in s or '[]' in s)


Solution.isValid("{}[]")
