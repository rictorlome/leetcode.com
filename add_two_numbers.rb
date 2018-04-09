# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
    sum = reverse_arr_and_combine(get_arr_of_nums(l1)) + reverse_arr_and_combine(get_arr_of_nums(l2))
    reverse_sum_and_llify(sum)
end

def get_arr_of_nums(node)
    res = []
    while node != nil
        res << node.val
        node = node.next
    end
    res
end

def reverse_arr_and_combine(arr)
    arr.reverse.map {|n| n.to_s}.join('').to_i
end    

def reverse_sum_and_llify(sum)
    nums = sum.to_s.split('').reverse.map {|el| el.to_i}
    i = 0
    res = ListNode.new(nums[0])
    cur = res
    while i < nums.length-1
        i += 1
        cur.next = ListNode.new(nums[i])
        cur = cur.next
    end    
    res
end   
