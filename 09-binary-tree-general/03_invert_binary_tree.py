"""[[ EASY ]]"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Algorithm:
            swap the left and the right nodes of the root.
            use recursion to invert the left, and the right subtrees.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
