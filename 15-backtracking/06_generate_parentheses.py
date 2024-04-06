"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _is_well_formed(self, stack):
        s = []
        for p in stack:
            if p == '(':
                s.append(p)
            else:
                # p is ')'
                if not s or s.pop() != '(':
                    return False
        return all([p == '(' for p in s])


    def _get_well_formed_parenthesis(self, parenthesis, store, result, history):
        if not parenthesis and store not in result:
            result.append(store)
        else:
            for i in range(len(parenthesis)):
                p = parenthesis[i]
                stack = store + p
                new_parenthesis = parenthesis[:i]+parenthesis[i+1:]
                if (stack, new_parenthesis) not in history and self._is_well_formed(stack):
                    history.add((stack, new_parenthesis))
                    self._get_well_formed_parenthesis(new_parenthesis, stack, result, history)

    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = '()' * n
        result = []
        self._get_well_formed_parenthesis(parenthesis, '', result, set())
        return result #[''.join(res) for res in result]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(6))
