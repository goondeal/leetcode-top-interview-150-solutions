"""[[ MEDIUM ]]"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        Algorithm:
            A simple solution is:
                1) Start a new list.
                2) Loop over the old list searching for nodes < [x] and put them in the new list.
                3) Loop over the old list again searching for nodes >= [x] and put them in the new list.
                4) Re-assign and return the head.
            
            Time Complexity: O(n)
            Time Complexity: O(n)
        '''
        if head:
            h = None # ListNode(val=head.val)
            node = h
            n = head
            while n:
                if n.val < x:
                    if node:
                        node.next = ListNode(val=n.val)
                        node = node.next
                    else:
                        node = ListNode(val=n.val)
                        h = node
                n = n.next
            n = head
            while n:
                if n.val >= x:
                    if node:
                        node.next = ListNode(val=n.val)
                        node = node.next
                    else:
                        node = ListNode(val=n.val)
                        h = node
                n = n.next
            head = h
            return head
