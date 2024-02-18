"""[[ EASY ]]"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthes_pairs = {')': '(', '}': '{', ']': '['}
        for c in s:
            # if c is a closing parenthes
            if c in parenthes_pairs:
                try:
                    last_element = stack.pop()
                    if last_element != parenthes_pairs.get(c):
                        return False
                except:
                    return False
            else:
                # c is an opening parenthes
                stack.append(c)

        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))
