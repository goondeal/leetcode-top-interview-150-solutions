"""[[ EASY ]]"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        Approach:
            Brute force algorithm of adding binaries.
        
        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
        '''
        result = []
        carry = 0
        
        m, n = len(a), len(b)
        a, b = a[::-1], b[::-1]
        for i in range(max(m, n)):
            digit_a = int(a[i]) if i < m else 0
            digit_b = int(b[i]) if i < n else 0
            
            summ = digit_a + digit_b + carry
            carry, res = divmod(summ, 2)
            result.append(res)
        if carry:
            result.append(carry)
        
        return ''.join([str(d) for d in result[::-1]])


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('1010', '1011'))
    print(s.addBinary('1', '11'))
