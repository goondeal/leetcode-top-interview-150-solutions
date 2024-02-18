"""[[ EASY ]]"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = [root.val]
        levels = [[root]]
        for group in levels:
            level = []
            for node in  group:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                levels.append(level)
                avg = sum([n.val for n in level]) / len(level)
                result.append(avg)
        return result
