"""[[ MEDIUM ]]"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach:
            1) collect the node values in a list.
            2) Sort values list.
            3) reassign the sorted values to the nodes in order.
        Notes:
            - A heap data structure could be used instead of a list to improve performance.
        Time Complexity: O(nlg(n))
        Space Complexity: O(n)
        '''
        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        vals.sort()
        node = head
        for val in vals:
            node.val = val
            node = node.next
        return head
