"""[[ EASY ]]"""
from typing import Optional

# Definition for a binary tree TreeNode.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    https://leetcode.com/problems/symmetric-tree/discuss/4566591/Nice-and-clear-beats-89.91
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            if not left or not right: 
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left,root.right)