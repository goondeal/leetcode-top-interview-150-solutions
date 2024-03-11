"""[[ MEDIUM ]]"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _collect_zigzag(self, level, result, ltr=True):
        if level:
            n = len(level)
            result.append([level[i if ltr else n-1-i].val for i in range(n)])
            children = []
            for node in level:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            self._collect_zigzag(children, result, ltr=not ltr)
            

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Approach:
            Brute-force approch.
            Same as collecting levels but with swapping the direction of collection.

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        result = []
        if root:
            self._collect_zigzag([root], result)
        return result
