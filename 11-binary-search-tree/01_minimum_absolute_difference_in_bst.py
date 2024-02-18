"""[[ EASY ]]"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _collect_in_order(self, root, l):
        if root:
            self._collect_in_order(root.left, l)
            l.append(root.val)
            self._collect_in_order(root.right, l)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        self._collect_in_order(root, l=values)
        min_diff = values[1] - values[0]
        for i in range(1, len(values)-1):
            d = values[i+1] - values[i]
            if d < min_diff:
                min_diff = d
        return min_diff

            



if __name__ == '__main__':
    t = TreeNode(236)
    t.left = TreeNode(104)
    t.right = TreeNode(701)

    t.left.right = TreeNode(227)
    t.right.right = TreeNode(911)

    s = Solution()
    print(s.getMinimumDifference(t))
