/* 
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.


EXAMPLE:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

SULUTION:
Get an array of intergers 
remove all the duplicates number on the array 

the order of the element should be the same 
and return the number of all the same elements in the array 
*/

function removeDuplicates(nums: Array<number | string>): number {
    let result: Array<number | string> = []
    let k: number = 0

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== nums[i + 1]) {
            result.push(nums[i])
        } else {
            result.push('_')
            result.slice(i, 1)
        }
    }

    for (let i = 0; i < result.length; i++) {
        if (result[i] !== '_') {
            k++
        }
    }
    console.log(nums)
    return k
};