"""[[ MEDIUM ]]"""
class MinStack:
    def __init__(self):
        self.stack = []
        self._min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)
        
    def pop(self) -> None:
        if self.stack.pop() == self._min_stack[-1]:
            self._min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self._min_stack[-1]
