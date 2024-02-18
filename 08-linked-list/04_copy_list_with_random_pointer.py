"""[[ MEDIUM ]]"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy the list state
        state = []
        node = head
        i = 0
        l_dict = {}
        while node is not None:
            l_dict[id(node)] = i
            i += 1
            state.append([node.val, node.random])
            node = node.next
        
        # Construct new list from the copied state
        if not state:
            return None
        h = Node(x=state[0][0])
        history = {0: h}
        n = h
        for i in range(1, len(state)):
            tmp = Node(x=state[i][0])
            n.next = tmp
            n = n.next
            history[i] = n
        n = h
        i = 0
        while n is not None:
            random_index = l_dict[id(state[i][1])] if state[i][1] else None
            if random_index is not None:
                n.random = history[random_index]
            n = n.next
            i += 1
        return h
        