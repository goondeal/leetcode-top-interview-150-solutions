"""[[ EASY ]]"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _search(self, node, sum, target):
        if node:
            if node.left and self._search(node.left, sum+node.val, target):
                return True
            if node.right and self._search(node.right, sum+node.val, target):
                return True
            if not node.left and not node.right and sum + node.val == target:
                return True
            
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._search(root, 0, targetSum)


if __name__ == '__main__':
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.right = TreeNode(8)

    t.left.left = TreeNode(11)
    t.left.left.left = TreeNode(7)
    t.left.left.right = TreeNode(2)


    s = Solution()
    print(s.hasPathSum(t, targetSum=22))
