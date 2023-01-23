###############
# Description #
###############

# Difficulty: medium

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains
# a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:

#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.


############
# Solution #
############

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    res = ListNode(0, None)
    curr = res
    carry = 0
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        sum = l1_val + l2_val + carry
        carry = sum // 10
        curr.next = ListNode(sum % 10, None)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return res.next


# Official solution:
# https://leetcode.com/problems/add-two-numbers/solutions/127833/add-two-numbers/

#########
# Tests #
#########

# Helpers


def list_to_arr(l: Optional[ListNode]) -> List[int]:
    res = []
    while l is not None:
        res.append(l.val)
        l = l.next
    return res


l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
assert list_to_arr(add_two_numbers(l1, l2)) == [7, 0, 8]

l3 = ListNode(7, ListNode(8, ListNode(9, None)))
l4 = ListNode(4, ListNode(3, None))
assert list_to_arr(add_two_numbers(l3, l4)) == [1, 2, 0, 1]

l5 = ListNode(0, None)
l6 = ListNode(0, None)
assert list_to_arr(add_two_numbers(l5, l6)) == [0]

print("All tests passed :)")
