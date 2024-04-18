"""[[ MEDIUM ]]"""
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def _is_same_val(self, grid: List[List[int]]) -> bool:
        val = grid[0][0]
        return all([e == val for row in grid for e in row])

    def construct(self, grid: List[List[int]]) -> 'Node':
        '''
        Approach:
            Follow the instructions:
            1) If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
            2) If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
            3) Recurse for each of the children with the proper sub-grid.
        
        Time Complexity: O(nlg(n))
        Space Complexity: O(nlg(n))
        '''
        if self._is_same_val(grid):
            return Node(
                val=grid[0][0],
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None,
            )
        else:
            mid = len(grid) // 2
            root = Node(val=1, isLeaf=0)
            root.topLeft = self.construct([row[:mid] for row in grid[:mid]])
            root.topRight = self.construct([row[mid:] for row in grid[:mid]])
            root.bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
            root.bottomRight = self.construct(
                [row[mid:] for row in grid[mid:]])
            return root
