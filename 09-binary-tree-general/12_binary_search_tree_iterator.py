"""[[ MEDIUM ]]"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    '''
    Approach:
        Since there are only 2 operations: "hasNext" and "next",
        Construct a list to store the tree inorder traversing and use a pointer to track the next value index.
    
    Time Complexity:
        Initialization: O(n)
        next and hasNext: O(1)
    
    Space Complexity: O(n)
    '''
    def __init__(self, root: Optional[TreeNode]):
        self._list = []
        self._build_list_from_tree(root, self._list)
        self._next_index = 0

    def _build_list_from_tree(self, root, l):
        if root:
            if root.left:
                self._build_list_from_tree(root.left, l)
            l.append(root.val)
            if root.right:
                self._build_list_from_tree(root.right, l)

    def next(self) -> int:
        self._next_index += 1
        return self._list[self._next_index-1]

    def hasNext(self) -> bool:
        return self._next_index < len(self._list)
