"""[[ HARD ]]"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def _max_sum(self, node, result):
    #     # print(node.val, result)
    #     paths = []
    #     if node.left:
    #         sum_left = self._max_sum(node.left, result)
    #         paths.append(sum_left)
    #     if node.right:
    #         sum_right = self._max_sum(node.right, result)
    #         paths.append(sum_right)
    #     if paths:
    #         result.append(node.val + max(max(paths), sum(paths)))
    #     return node.val + (max(paths) if paths else 0)
        
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_lateral = float('-inf')
        def _max_sum(node):
            paths = []
            nonlocal max_lateral
            max_lateral = max(max_lateral, node.val)
            if node.left:
                sum_left = _max_sum(node.left)
                paths.append(sum_left)
            if node.right:
                sum_right = _max_sum(node.right)
                paths.append(sum_right)
            if paths:
                max_lateral = max(max_lateral, node.val + max(max(paths), sum(paths)))
                return max(node.val, node.val + max(paths))
            return node.val

        res = _max_sum(root)
        return max(res, max_lateral)


if __name__ == '__main__':
    s = Solution()
    print(s.maxPathSum(TreeNode(1))) # 1
    print(s.maxPathSum(TreeNode(1, left=TreeNode(2), right=TreeNode(3)))) # 6
    print(s.maxPathSum(TreeNode(1, left=TreeNode(-2), right=TreeNode(-3)))) # 1
    print(s.maxPathSum(TreeNode(-1, left=TreeNode(-2), right=TreeNode(-3)))) # -1
    print(s.maxPathSum(TreeNode(1, right=TreeNode(3)))) # 4
    print(s.maxPathSum(TreeNode(-2, right=TreeNode(1)))) # 4
    print(s.maxPathSum(TreeNode(-10, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))))) # 42
    print(s.maxPathSum(TreeNode(3, left=TreeNode(7, left=TreeNode(2, left=TreeNode(8), right=TreeNode(5))), right=TreeNode(4, left=TreeNode(4), right=TreeNode(6, left=TreeNode(9), right=TreeNode(3)))))) # 42
    print(s.maxPathSum(TreeNode(-3, left=TreeNode(-7, left=TreeNode(-2, left=TreeNode(-8), right=TreeNode(-5))), right=TreeNode(-4, left=TreeNode(-4), right=TreeNode(-6, left=TreeNode(-9), right=TreeNode(-3)))))) # 42
    # [1,-2,-3,1,3,-2,null,-1] # 3
    # [-1,5,null,4,null,null,2,-4] # 11