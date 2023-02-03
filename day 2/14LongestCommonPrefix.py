""" 

Input: strs = ["flower", "flow", "flight"]
Output: "fl" 


if the fist letter of the first word is equal to the first letter of the second letter
add it to one array.

"""


class Solution:
    def longestCommonPrefix(strs):
        res = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                print(res)
        print(res)


Solution.longestCommonPrefix(["flower", "flow", "flight"])
