/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort((a,b) => {return a-b})
    for (let i = 0; i < nums.length+1;i++){
        if(nums[i] != i) {return i}
    }
    
};