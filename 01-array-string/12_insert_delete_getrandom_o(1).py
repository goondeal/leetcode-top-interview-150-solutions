"""[[ MEDIUM ]]"""
import random


class RandomizedSet:
    '''
    Approach:
        Using a HashSet will be enough for insert and remove operations with O(1) time complexity,
        But there is no way to achieve "getRandom" on a set in O(1).

        So, use a list to perform getRandom in O(1). It is also O(1) in insertion, but it is O(n) in remove.
        But, if we could place the value to be removed at the end of the list before removing it, Then, we are removing the last element of the list, and "remove" will take O(1).

        Acheive that by Using a HashMap (dictionary) to store index for each value. This way we will be able to do insert, remove, and getRandom in O(1) time complexity.
    
    Time Complexity: O(1)
    Space Complexity: O(n)
    '''
    def __init__(self):
        self._dict = {}
        self._vals = []

    def insert(self, val: int) -> bool:
        # If val already exists, return false
        if val in self._dict:
            return False

        # save val in _vals, and save val in _dict with its index (always will be len(_vals)-1)
        self._vals.append(val)
        self._dict[val] = len(self._vals) - 1

        return True

    def remove(self, val: int) -> bool:
        # If val does not exist, return False
        if val not in self._dict:
            return False

        # Swap the places of val and the last index of _vals, so that the remove operation takes O(1).
        # Get index of val in _vals
        idx = self._dict[val]
        # Swap with the last element in _vals
        self._vals[idx], self._vals[-1] = self._vals[-1], self._vals[idx]
        # Update the index of the other swapped value in _dict.
        self._dict[self._vals[idx]] = idx
        # Remove val from _dict, and _vals
        del self._dict[val]
        self._vals.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self._vals)
