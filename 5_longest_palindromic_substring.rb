# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Based on principle:
# char x , string s
# x s x -- is a palindrome iff s is. Empty string is a palindrome.
# x s y -- not a palindrome, check in constant time

def lps(s)
    return "" if s.empty?
    longest = [0,0]
    s.chars.each_with_index do |ch, idx|
        for i,j in [[idx, idx + 1], [idx, idx]]
            until s[i] != s[j]
                break if i < 0 || j >= s.length
                longest = [i,j] if longest[1] - longest[0] < j - i
                i -= 1
                j += 1
            end
        end
    end
    s[longest[0]..longest[1]]
end
