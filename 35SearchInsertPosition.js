/**
 * input = arr[1,2,3,4,7], n6
 * output = 4
 * for each arr n === arr[i] return index
 * else arr[i] > n   return index-1
 * 
 * Input: nums = [1,3,5,6], target = 5 -> Output: 2
 *
 *  */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let lo = 0, hi = nums.length; // we might need to inseart at the end
    while (lo < hi) { // breaks if lo == hi
        let mid = lo + Math.floor((hi - lo) / 2); // always gives the lower mid
        
        if (target > nums[mid]) {
            lo = mid + 1 // no way mid is a valid option
        } else {
            hi = mid // it might be possibe to inseart @ mid
        }
    }
    return lo;
};

console.log(searchInsert([1, 3, 5, 6], 2))
