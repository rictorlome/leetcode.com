# @param {Integer} n
# @return {String}
def count_and_say(n)
        if n == 1
            return "1"
        else
            return helper(count_and_say(n-1))
        end
end
        
def helper(str)
    count = 1
    cur = str[0]
    res = ""
    str.chars.drop(1).each do |ch|
        if cur == ch
            count += 1
        else
            res += count.to_s + cur
            count = 1
            cur = ch
        end
    end    
    res += count.to_s + cur 
end
