"""[[ MEDIUM ]]"""
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodes_dict = {id(node): 0}
        nodes = [node]
        
        for n in nodes:
            for neighbor in n.neighbors:
                if id(neighbor) not in nodes_dict:
                    nodes.append(neighbor)
                    nodes_dict[id(neighbor)] = len(nodes) - 1
        # Clone nodes with its values
        new_nodes = [Node(val=n.val) for n in nodes]
        # Clone the relations for the new nodes
        for i in range(len(nodes)):
            neighbors_pos = [nodes_dict[id(n)] for n in nodes[i].neighbors]
            new_nodes[i].neighbors = [new_nodes[pos] for pos in neighbors_pos]
        
        return new_nodes[0]
