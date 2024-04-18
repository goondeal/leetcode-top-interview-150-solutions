"""[[ MEDIUM ]]"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _collect_preorder(self, root: Optional[TreeNode], k: int, result: List[int] = []):
        if root:
            if root.left:
                self._collect_preorder(root.left, k=k, result=result)
            result.append(root.val)
            if root.right:
                self._collect_preorder(root.right, k=k, result=result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Approach:
            Traverse the tree preorder and collecting its values in a [result] list.
            Return result[k-1], as k is 1-indexed

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        result = []
        self._collect_preorder(root, k, result)
        return result[k-1]
