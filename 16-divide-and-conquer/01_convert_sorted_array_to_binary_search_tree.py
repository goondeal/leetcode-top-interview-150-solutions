"""[[ EASY ]]"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _build_tree(self, nums, i, j):
        if j > i:
            if j-i == 1:
                return TreeNode(nums[i])
            mid = (i+j) // 2
            root = TreeNode(nums[mid])
            root.left = self._build_tree(nums, i, mid)
            root.right = self._build_tree(nums, mid+1, j)
            return root
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self._build_tree(nums, 0, len(nums))
        return root
