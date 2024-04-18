"""[[ MEDIUM ]]"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Algorithm:
            Brute force -> The list is sorted. So, loop through the list skipping any redundent adjacent nodes.
            paying attention to the edge cases.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        prev = None
        current = head
        while current and current.next:
            # search for redundent nodes
            if current.val == current.next.val:
                # Get the first different value.
                while current.next and current.val == current.next.val:
                    current.next = current.next.next
                if prev and prev.val != current.val:
                    prev.next = current.next
                    current = prev.next
                else:
                    prev = current.next
                    head = prev
                    current = prev
            # if not: just move the pointers
            else:
                prev = current
                current = current.next
        return head



# testcases
# [1,2,3,3,4,4,5] -> [1,2,5]
# [1,1,1,2,3] -> [2,3]
# [1,1,1,2,2,3] -> [3]
# [1,2,2] -> [1]
