"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _get_comb_sum(self, candidates, target, store, result):
        for num in candidates:
            if target == num:
                res = sorted(store + [num])
                if res not in result:
                    result.append(res)
            elif target > num:
                t = target - num
                self._get_comb_sum(candidates, t, store + [num], result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self._get_comb_sum(candidates, target, [], result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], target=7))
    print(s.combinationSum([2, 3, 5], target=8))
    print(s.combinationSum([2], target=1))
    print(s.combinationSum([1, 2, 3], target=6))
