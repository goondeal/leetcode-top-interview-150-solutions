"""[[ HARD ]]"""
class Solution:
    def calculate(self, s: str) -> int:
        def get_matching_closing_pair_index(l, start=0):
            s = ['(']
            i = start
            while s and i < len(l):
                if l[i] == ')':
                    s.pop()
                elif l[i] == '(':
                    s.append('(')
                i += 1
            return i - 1
        
        def sum_list(l, start=0):
            result = 0
            i = start
            while i < len(l):
                e = l[i]
                if e == '-':
                    if isinstance(l[i+1], int):
                        result -= l[i+1]
                        i += 2
                    else:
                        closing_pair_idx = get_matching_closing_pair_index(l, i+2)
                        result -= sum_list(l[i+2: closing_pair_idx+1])
                        i = closing_pair_idx + 1
                elif isinstance(e, int):
                    result += e
                    i += 1
                elif e == '(':
                    closing_pair_idx = get_matching_closing_pair_index(l, i+1)
                    result += sum_list(l[i+1: closing_pair_idx+1])
                    i = closing_pair_idx + 1
                else:
                    i += 1 
            return result
            
        stack = []
        num = ''
        for c in s:
            if c != ' ':
                if c.isdigit():
                    num += c
                else:
                    if num:
                        stack.append(int(num))
                        num = ''
                    stack.append(c)
        if num:
            stack.append(int(num))
        return sum_list(stack)