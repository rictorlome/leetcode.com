//input in this case is a string of chars either 'U' 'D' 'L' or 'R'. ex "UDDDUUULRLRLRLRRRRLLUDLRUDLRUD"

var judgeCircle = function(moves) {
  var uCount = 0;
  var dCount = 0;
  var lCount = 0;
  var rCount = 0;
  for (var i = 0; i<moves.length; i++) {
    if (moves[i] === 'U') {
      uCount++;
    }
    if (moves[i] === 'D') {
      dCount++;
    }
    if (moves[i] === 'L') {
      lCount++;
    }
    if (moves[i] === 'R') {
      rCount++;
    }
  }
  // if ups equal downs && lefts equal rights, then the object is back where it started.
  if (uCount - dCount === 0 && lCount - rCount === 0) {
    return true;
  } else {
    return false;
  }    
}
