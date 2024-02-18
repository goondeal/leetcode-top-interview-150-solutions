"""[[ EASY ]]"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        n1, n2 = list1, list2
        result_head = result_tail = None

        def _append_node(node):
            nonlocal result_head
            nonlocal result_tail
            if result_head == None:
                result_head = node
                result_tail = node
            else:
                result_tail.next = node
                result_tail = result_tail.next

        while n1 != None or n2 != None:
            if n1 == None:
                _append_node(n2)
                n2 = n2.next
            elif n2 == None:
                self._append_node(n1)
                n1 = n1.next
            else:
                # both != None
                if n1.val < n2.val:
                    _append_node(n1)
                    n1 = n1.next
                else:
                    _append_node(n2)
                    n2 = n2.next

        return result_head
