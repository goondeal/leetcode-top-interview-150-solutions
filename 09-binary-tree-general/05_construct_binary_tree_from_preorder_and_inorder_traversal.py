"""[[ MEDIUM ]]"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Approach:
            - Like most binaary-tree problems, Delegate the heavy work to recursion.
            - Understand the base case first on a tree of 2 or 3 nodes.  

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        n = len(preorder)        
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(val=preorder[0])
        else:
            root = TreeNode(val=preorder[0])
            # get the root index in inorder to split at.
            inorder_root_index = 0
            for i in range(n):
                node = inorder[i]
                if node == preorder[0]:
                    inorder_root_index = i
                    break
            inorder_left = inorder[:inorder_root_index]
            inorder_right = inorder[inorder_root_index+1:]
            
            root.left = self.buildTree(preorder=preorder[1:1+len(inorder_left)], inorder=inorder_left)
            root.right = self.buildTree(preorder=preorder[1+len(inorder_left):], inorder=inorder_right)
            return root
