"""[[ MEDIUM ]]"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _get_path_num(self, node: Optional[TreeNode], path: List[str]) -> int:
        # Append node val to path.
        path.append(str(node.val))
        # If leaf, return the number
        if not node.left and not node.right:
            return int(''.join(path))
        else:
            # Not leaf, get the sum of left, and right paths.
            res = 0
            if node.left:
                res += self._get_path_num(node.left, path)
                path.pop()
            if node.right:
                res += self._get_path_num(node.right, path)
                path.pop()
            return res
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        Approach:
            Using depth first approach to find root-to-leef paths and a [path] list to track nodes values.
            Once you reached a leaf, get the number from the [path] list.
            Sum the numbers and return the result.

        
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        result = self._get_path_num(root, path=[])
        return result
