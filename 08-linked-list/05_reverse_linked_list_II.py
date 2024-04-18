"""[[ MEDIUM ]]"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next
        l, r = left-1, right-1
        new_vals = vals[:l] + vals[l:r+1][::-1] + vals[r+1:]
        
        i = 0
        node = head
        while node is not None:
            if l <= i <= r:
                node.val = new_vals[i]
            node = node.next
            i += 1
        return head
        
        