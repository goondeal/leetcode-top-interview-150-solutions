"""[[ MEDIUM ]]"""


class Solution:
    def _get_next_index(self, row: int) -> int:
        return row + max(0, row-2)
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = []
        for _ in range(numRows):
            l.append([])
        
        arr, step = 0, -1
        boundries = {0, numRows-1}
        for c in s:
            l[arr].append(c)
            if arr in boundries:
                step *= -1
            arr += step
        
        result = []
        for arr in l:
            result += arr
        
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    # print(s.convert('PAYPALISHIRING', numRows=3))
    # print(s.convert('PAYPALISHIRING', numRows=4))
    # print(s.convert('A', numRows=1))
    print(s.convert('AB', numRows=1))
