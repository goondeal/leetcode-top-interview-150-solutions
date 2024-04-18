"""[[ MEDIUM ]]"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        Approach:
            Same as the orevious one.  

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        n = len(inorder)        
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(val=postorder[0])
        else:
            root = TreeNode(val=postorder[-1])
            # get the root index in inorder to split at.
            inorder_root_index = 0
            for i in range(n):
                node = inorder[i]
                if node == root.val:
                    inorder_root_index = i
                    break
            inorder_left = inorder[:inorder_root_index]
            inorder_right = inorder[inorder_root_index+1:]
            
            root.left = self.buildTree(postorder=postorder[:n-len(inorder_right)-1], inorder=inorder_left)
            root.right = self.buildTree(postorder=postorder[-1-len(inorder_right):-1], inorder=inorder_right)
            return root
