""" 
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Pseuo code 

for each number in list sum others numbers, if the nuber return the 
target return the two number

"""


class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, number in enumerate(nums):
            rem = target - number
            if rem in nums and index != nums.index(rem):
                print([index, nums.index(rem)])
                break


Solution.twoSum([3, 2, 4], 6)
