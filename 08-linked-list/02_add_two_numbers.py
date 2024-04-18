"""[[ MEDIUM ]]"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _linked_list_to_int(self, l):
        node = l
        result = []
        while node is not None:
            result.append(node.val)
            node = node.next
        return int(''.join([ str(d) for d in result[::-1]]))
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self._linked_list_to_int(l1)
        num2 = self._linked_list_to_int(l2)
        digits = list(str(num1 + num2)[::-1])
        digits = [int(d) for d in digits]
        head = ListNode(val=digits[0])
        node = head
        for i in range(1, len(digits)):
            n = ListNode(val=digits[i])
            node.next = n
            node = node.next
        return head
            
        