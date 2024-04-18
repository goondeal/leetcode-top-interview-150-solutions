"""[[ HARD ]]"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Approach:
            Collect all node values in a list.
            Then, traverse the linkedlist and assign each node value to its corresponding group node value from the stored values

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        n = 0 # list length
        node = head
        vals = []
        while node:
            # track the list length
            n += 1
            # collect node value
            vals.append(node.val)
            # move to the next list node
            node = node.next
        
        
        mod = n % k
        node = head
        # for each node get the value of its corresponding group node.
        for i in range(n-mod):
            group, mod = divmod(i, k)
            # corrsponding group node index
            idx = group * k + k - i - 1 + k * group
            node.val = vals[idx]
            node = node.next
        return head
