"""[[ MEDIUM ]]"""
class Solution:
    def simplifyPath(self, path):
        stack = []
        parts = [part for part in path.split('/') if part not in {'', '.'}]
        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
        

if __name__ == '__main__':
    # path = '//home/../'
    path = '/home/'
    s = Solution()
    result = s.simplifyPath(path)
    print('result =', result)
