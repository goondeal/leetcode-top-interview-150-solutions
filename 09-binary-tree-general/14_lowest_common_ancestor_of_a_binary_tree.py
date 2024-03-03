"""[[ MEDIUM ]]"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _assign_parents(self, root: 'TreeNode'):
        if root.left:
            setattr(root.left, 'parent', root)
            # root.left.parent = root
            self._assign_parents(root.left)
        if root.right:
            root.right.parent = root
            self._assign_parents(root.right)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self._assign_parents(root)
        
        p_ancestors = []
        node = p
        while node:
            p_ancestors.append(node)
            node = node.parent
        
        node = q
        while node:
            for a in p_ancestors:
                if node is a:
                    return a
            node = node.parent
            