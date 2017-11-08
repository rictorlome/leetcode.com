                                                                     
                                                                     
                                                                     
                                             
/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort(compareNumbers);
    var sum = 0;
    for (var i = 0; i<nums.length; i++) {
        if (i % 2 === 0) {
            sum += nums[i]
        }
    }
    return sum;    
};

var compareNumbers = function(a,b) {
    return a-b;
}
