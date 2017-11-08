/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
  //assign inputs to variables because you cannot run toString on a number.
  var X = x;
  var Y = y;  
  //create strings of 0s and 1s for original numbers.
  var binX = X.toString(2);
  var binY = Y.toString(2);
  var count = 0;
  
  //create arrays from binary strings 
  var binXarr = binX.split('');
  var binYarr = binY.split('');
  
  //see below for equalizeWithZeros function. this adds 0s to the front of the shorter array until their lengths are the same.
  if (binX.length < binY.length) {
    binXarr = equalizeWithZeros(binX,binY).split('');
  } else if (binX.length > binY.length) {
    binYarr = equalizeWithZeros(binX,binY).split('');
  }
 
  //for loop runs through the now equally sized arrays, checking if values are the same. if not, count ++.
  for (var i = 0; i<binXarr.length; i++) {
    if (binXarr[i] !== binYarr[i]) {
      count++;
    }
  }
  return count;
}

function equalizeWithZeros(s1, s2) {
  //converts strings to arrays.
  arrS1 = s1.split('');
  arrS2 = s2.split(''); 
  
  // if s1 is longer, add 0s to front of arr2 until the arrays are the same size. else does same for arr1 if s2 is longer.
  // then converts the array back to a string and returns that string. (i guess this part had no point, if I'm going to split it again)
  if (s1.length > s2.length) {
    while (arrS1.length > arrS2.length) {
      arrS2.unshift(0);
    }
    return arrS2.join('');
  } else {
    while (arrS1.length < arrS2.length) {
      arrS1.unshift(0);
    }
    return arrS1.join('');
  }
}
