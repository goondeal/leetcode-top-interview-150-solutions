"""[[ MEDIUM ]]"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _collect_levels(self, level, result):
        if level:
            result.append([node.val for node in level])
            children = []
            for node in level:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            self._collect_levels(children, result)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Approach:
            Brute-force approch.

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        result = []
        if root:
            self._collect_levels([root], result)
        return result
