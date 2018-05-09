# Examples:

# Given "abcabcbb", the longest is "abc", so return 3.
# Given "bbbbb", the longest is "b", so return 1.
# Given "pwwkew", the longest is "wke", so return 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    return 0 if s.empty?
    i, j = 0, 0
    longest = 1
    seen = {}

    while j < s.length
        cur = s[j]
        if seen[cur] && seen[cur].between?(i,j)
            i = seen[cur] + 1
        end
        longest = j - i + 1 if j - i + 1 > longest
        seen[cur] = j
        j += 1
    end
    longest
end
