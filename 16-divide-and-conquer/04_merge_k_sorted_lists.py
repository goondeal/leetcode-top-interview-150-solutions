"""[[ HARD ]]"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Approach:
            Since the linked-lists are sorted in ascending order, the minimum element of all node of all linked-lists will always be a head of them (always at the start).
            Loop through [lists] to find the minimum head value, append that head to the result and then move the head pointer to head.next
            Repeat till you reach the end of all lists
            
        Time Complexity: O(n*k)
        Space Complexity: O(1)
        '''
        k = len(lists)
        if not k:
            return None
        
        head = None # of the result
        node = head # tail of the result
        
        while any(lists):
            # Get minimum number of the lists
            min_head_idx = None
            for i in range(k):
                h = lists[i]
                if h and (min_head_idx is None or h.val < lists[min_head_idx].val):
                    min_head_idx = i
            
            min_head = lists[min_head_idx]
            if head:
                node.next = min_head
                node = node.next
            else:
                head = min_head
                node = head
            # move the head pointer of the appended-head linked-list
            lists[min_head_idx] = min_head.next
        return head
