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
    cur1, cur2 = l1, l2
    carried = 0
    res = ListNode.new(0)
    cur = res
    while cur1 != nil || cur2 != nil
        cur1 == nil ? s1 = 0 : s1 = cur1.val
        cur2 == nil ? s2 = 0 : s2 = cur2.val
        sum = s1 + s2 + carried
        carried, cur.val = sum/10, sum%10
        if (cur1 && cur1.next != nil) || (cur2 && cur2.next != nil)
            cur.next = ListNode.new(0)
            cur = cur.next
        end
        cur1 == nil ? cur1 = nil : cur1 = cur1.next
        cur2 == nil ? cur2 = nil : cur2 = cur2.next
    end

    cur.next = ListNode.new(carried) if carried != 0
    res
end
