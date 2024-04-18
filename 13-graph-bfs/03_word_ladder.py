"""[[ HARD ]]"""
from typing import List


class Solution:
    def _calc_diff(self, w1, w2):
        return sum([w1[i] != w2[i] for i in range(len(w1))])

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        words = wordList + [beginWord]
        n = len(words)
        
        graph = {endWord: 1}
        queue = [endWord]
        history = {endWord}
        for node in queue:
            for w in words:
                if w not in history and self._calc_diff(node, w) == 1:
                    queue.append(w)
                    history.add(w)
                    graph[w] = min(graph.get(w, n + 1), 1 + graph[node])
                    if w == beginWord:
                        return graph[w]
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength(beginWord="hit", endWord="cog",
          wordList=["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(s.ladderLength(beginWord="hit", endWord="hot",
          wordList=["hot", "dot", "dog", "lot", "log", "cog"]))  # 1
    print(s.ladderLength(beginWord="hit", endWord="cog",
          wordList=["hot", "dot", "dog", "lot", "log"]))  # 0
