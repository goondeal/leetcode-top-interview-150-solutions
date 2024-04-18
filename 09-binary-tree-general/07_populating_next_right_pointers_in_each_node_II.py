"""[[ MEDIUM ]]"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def _connect(self, nodes):
        if nodes:
            # by the last line, children will contain the next level nodes.
            children = []
            for i in range(len(nodes)-1):
                # connect each node to the next
                nodes[i].next = nodes[i+1]
                # push its children to children list
                if nodes[i].left:
                    children.append(nodes[i].left)
                if nodes[i].right:
                    children.append(nodes[i].right)
            # append left and right of the last node
            if nodes[-1].left:
                    children.append(nodes[-1].left)
            if nodes[-1].right:
                children.append(nodes[-1].right)
            # connect the next level
            self._connect(children)    
        
    def connect(self, root: 'Node') -> 'Node':
        '''
        Approach:
            use breadth-first traversal to group each level and connect each node to the next node in the level

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        if root:
            self._connect([root])
        return root
