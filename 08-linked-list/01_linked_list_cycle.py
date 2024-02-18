"""[[ EASY ]]"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node != None:
            if getattr(node, 'visited', False):
                return True
            node.visited = True
            node = node.next    
        