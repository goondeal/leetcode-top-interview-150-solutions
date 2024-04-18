"""[[ MEDIUM ]]"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Algorithm:
            1) Skip wasted rotations by reassigning k to k%n where n is the list length.
            2) Notice that any list rotated by k where k < n will be as if you replaced the slice (from (n-k)th element to the end) at the start of the list.
            3) Do that plan.

        Time Complexity: O(n)
        space Complexity: O(1)
        '''
        if head:
            # Calc list length
            n = 0
            node = head
            while node:
                node = node.next
                n += 1
            # Skip wasted rotates
            # if k = n then the rotated list will be at the same order as it was originally,
            # and this is a wasted effort.
            k = k % n
            if k:
                node = head
                for _ in range(n-k-1):
                    node = node.next                
                head2 = node.next
                holder = node.next
                node.next = None
                while head2.next:
                    head2 = head2.next
                head2.next = head
                head = holder
        return head
