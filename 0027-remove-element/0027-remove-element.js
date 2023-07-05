/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let current = 0;
    let k = 0;
    while(current < nums.length){
        if (nums[current] != val){
            nums[k] = nums[current]
            k++
        }
       current++}
    return k
};

    
        
    
    
    
    
    
    