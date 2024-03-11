"""[[ MEDIUM ]]"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _collect_right_side(self, level, result):
        if level:
            result.append(level[-1].val)
            children = []
            for node in level:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            self._collect_right_side(children, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Approach:
            Brute-force approch where you pick the right-most node of each level.

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        result = []
        if root:
            self._collect_right_side([root], result)
        return result
