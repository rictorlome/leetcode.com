                                             
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    var outputArrayOfWords = [];
    //creates an array of words, each element is one word.
    var arrayOfWords = s.split(' ');
    //iterates through arrayOfWords. for each element...
    for (var i = 0; i<arrayOfWords.length; i++) {
        var word = arrayOfWords[i];
        //create an array of letters for every word.
        var arrayOfLetters = word.split('');
        //reverse and join the array of letters to form a string with the letters reversed
        var backwardsWord = arrayOfLetters.reverse().join('');
        outputArrayOfWords.push(backwardsWord);
    }
    return outputArrayOfWords.join(' ');
};
