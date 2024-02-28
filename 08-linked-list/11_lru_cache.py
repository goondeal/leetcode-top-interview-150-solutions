"""[[ MEDIUM ]]"""
class LRUCache:
    class Node:
        def __init__(self, key, val, prev=None, next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next
        
        
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._dict = {}
        self._head = None
        self._tail = None
    
    def get_size(self):
        return len(self._dict)
    
    def _add_node(self, node):
        # Add at the start
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._head.prev = node
            node.next = self._head
            node.prev = None
            self._head = node
    
    def _delete_node(self, node):
        prev, next = node.prev, node.next
        if not prev and not next: # only node
            self._head = None
            self._tail = None
        
        elif prev and not next: # tail
            prev.next = next
            self._tail = prev
        
        elif not prev and next: # head
            next.prev = prev
            self._head = next
        
        else: # middle node
            prev.next = next
            next.prev = prev

        node.prev = None
        node.next = None
        return node
    
    def get(self, key: int) -> int:
        if key in self._dict:
            node = self._dict[key]
            del self._dict[key]
            # make head
            self._add_node(self._delete_node(node))
            self._dict[key] = self._head
            return self._head.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            node = self._dict[key]
            del self._dict[key]
            self._delete_node(node)
        
        if self.get_size() == self.capacity:
            del self._dict[self._tail.key]
            self._delete_node(self._tail)

        self._add_node(self.Node(key, value))
        self._dict[key] = self._head
