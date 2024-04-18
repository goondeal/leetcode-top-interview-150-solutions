"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _is_valid_path(self, graph, c, visited, valid_paths):
        dependants = graph.get(c)
        if not dependants or c in valid_paths:
            return True
        for d in dependants:
            if d in visited:
                return False
            res = self._is_valid_path(graph, d, visited|{d}, valid_paths)
            if not res:
                return False
        valid_paths |= set(dependants+[d])
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = {}
        for next_, prev in prerequisites:
            if next_ in course_dict:
                course_dict[next_].append(prev)
            else:
                course_dict[next_] = [prev]
        
        valid_paths = set()
        for next_, prev in prerequisites:
            if not self._is_valid_path(course_dict, next_, {next}, valid_paths):
                print(next_, prev)
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    # print(s.canFinish(numCourses=2, prerequisites=[[1, 0]])) # true
    # print(s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])) # false
    # print(s.canFinish(numCourses=13, prerequisites=[[1,2],[2,3],[2,10],[3,4],[4,5],[4,11],[5,1]])) # false
    print(s.canFinish(numCourses=4, prerequisites=[[2,0],[1,0],[3,1],[3,2],[1,3]])) # false
