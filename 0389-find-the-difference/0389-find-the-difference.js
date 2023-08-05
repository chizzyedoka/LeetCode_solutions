/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    sArray = s.split('')
    tArray = t.split('')
    sArray.sort()
    tArray.sort()
    for(let i = 0; i < t.length;i++){
        if (sArray[i] !== tArray[i]) return tArray[i]
    }
    return tArray[ t.length-1]
    
    
};