"""[[ MEDIUM ]]"""
class Solution:
    def evalRPN(self, tokens):
        def apply_fun(x, y, fun):
            return fun(x, y)
        
        functions = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__truediv__}
        stack = []
        ops_set = set(functions.keys())
        for token in tokens:
            if token in ops_set:
                y, x = stack.pop(), stack.pop()
                result = apply_fun(x, y, functions[token])
                stack.append(int(result) if token == '/' else result)
            else:
                stack.append(int(token))
        return stack[-1]
    
if __name__ == '__main__':
    tokens = ['4', '13', '5', '/', '+']
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = Solution()
    result = s.evalRPN(tokens)
    print('result =', result)
