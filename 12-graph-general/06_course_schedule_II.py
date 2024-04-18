"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _is_valid_path(self, graph, c, visited, valid_paths, course_path):
        dependants = graph.get(c)
        if not dependants or c in valid_paths:
            return True
        
        for d in dependants:
            if d in visited:
                return False
            res = self._is_valid_path(graph, d, visited|{d}, valid_paths, course_path)
            if not res:
                return False
        
        course_path += [x for x in dependants+[c] if x not in valid_paths]
        # course_path.append(c)
        valid_paths |= set(dependants+[c])
        return True

    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        
        course_dict = {}
        for next_, prev in prerequisites:
            if next_ in course_dict:
                course_dict[next_].append(prev)
            else:
                course_dict[next_] = [prev]
        
        # print(course_dict)
        valid_paths = set()
        course_path = []
        for c in course_dict:
            if not self._is_valid_path(course_dict, c, {c}, valid_paths, course_path):
                # print(next_, prev)
                return []
        if len(course_path) < numCourses:
            course_path += list(set(range(numCourses)) - set(course_path))
        return course_path
