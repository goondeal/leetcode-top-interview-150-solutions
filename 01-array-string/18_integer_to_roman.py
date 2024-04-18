"""[[ MEDIUM ]]"""
class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        Algorithm:
            Once you created the units list that contains 
            the numbers units with its corresponding letters ordered descendingly,
            Start to figure out what units that [num] consists of and how many of each unit.
        
            Time Complexity: O(1) # not sure
            space Complexity: O(1) # not sure
        '''
        units = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        i = 0
        result = []
        while num > 0:
            while num < units[i][0]:
                i += 1
            div, num = divmod(num, units[i][0])
            result += [units[i][1]] * div
        return ''.join(result)
