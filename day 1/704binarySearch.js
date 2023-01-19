/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 * https://leetcode.com/problems/binary-search/?envType=study-plan&id=algorithm-i
 */
var search = function (nums, target) {
    let result = -1
    nums.forEach((element, index) => {
        if (element === target) {
            result = index
        }
    });
    return result
};

console.log(search([-1, 0, 3, 5, 9, 12], 9))