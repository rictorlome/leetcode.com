                                                                                                                                                                                                                                                    
/**
 * @param {number} num
 * @return {number}
 */

var findComplement = function(num) {
    // assign number to variable so you can run toString on it. split that string into an array.
    var X = num;
    var xBinary = X.toString(2);
    var xBinaryArr = xBinary.split('');
    
    // this array will end up being the output
    var complArr = [];
    
    //iterate through array of strings of either "0" and "1". checks whether each index is "0", important to keep track of datatypes here.
    for (var i = 0; i<xBinaryArr.length; i++) {
        if (xBinaryArr[i] === "0") {
            complArr.push(1);            
        } else {
            complArr.push(0);
        }
    }
    //convert the array to a string so you can run parseInt on it.
    var complString = complArr.join('');
    //convert string of 0s and 1s back to an integer
    var int = parseInt(complString, 2)
    return int;
};
