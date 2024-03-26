"""[[ MEDIUM ]]"""
from functools import reduce
from typing import List


class Solution:
    def _get_path(self, graph, s, t, path, visited):
        for e, val in graph[s]:
            if e[-1] == t:
                path.append(val)
                return path
        visited.add(s)
        for e, val in graph[s]:
            if e[-1] not in visited:
                res = self._get_path(graph, e[-1], t, path+[val], visited)
                if res:
                    return res
        return None


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        var_dict = {}
        for i in range(n):
            e = equations[i]
            if e[0] in var_dict:
                var_dict[e[0]].append((e, values[i]))
            else:
                var_dict[e[0]] = [(e, values[i])]
            if e[1] in var_dict:
                var_dict[e[1]].append((e[::-1], 1/values[i]))
            else:
                var_dict[e[1]] = [(e[::-1], 1/values[i])]

        result = []
        for q in queries:
            if q[0] not in var_dict or q[1] not in var_dict:
                result.append(-1)
            elif q[0] == q[1]:
                result.append(1)
            else:
                res = None
                for e, val in var_dict[q[0]]:
                    if e == q:
                        res = val
                if res is not None:
                    result.append(res)
                else:
                    visited = set()
                    vals = []
                    res = self._get_path(var_dict, q[0], q[1], vals, visited)
                    result.append(reduce(lambda a, b: a*b, res) if res else -1)
        return result
