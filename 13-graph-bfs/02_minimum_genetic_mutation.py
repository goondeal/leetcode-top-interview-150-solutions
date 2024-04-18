"""[[ MEDIUM ]]"""
from typing import List


class Solution:
    def _find_min_mutations(self, gene, end_gene, graph, history, mutations_count):
        if end_gene in graph.get(gene, set()):
            return mutations_count + 1

        history.add(gene)
        res = []
        for g in graph.get(gene, set()):
            if g not in history:
                m = self._find_min_mutations(
                    g, end_gene, graph, history.copy(), mutations_count+1)
                if m != -1:
                    res.append(m)

        return min(res) if res else -1


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0

        graph = {}
        queue = [startGene]
        for gene in queue:
            valid_mutations = [g for g in bank if sum(
                [g[i] != gene[i] for i in range(8)]) == 1]
            graph[gene] = valid_mutations[:]
            queue += [m for m in valid_mutations if m not in graph]
        # print(graph)

        history = set()
        res = self._find_min_mutations(startGene, endGene, graph, history, 0)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minMutation(startGene="AACCGGTT",
          endGene="AACCGGTA", bank=["AACCGGTA"]))  # 1
    print(s.minMutation(startGene="AACCGGTT", endGene="AAACGGTA",
          bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 2
    print(s.minMutation(startGene="AACCTTGG", endGene="AATTCCGG",
          bank=["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]))  # -1
    print(s.minMutation(startGene="AACCGGTT", endGene="AAACGGTA",
          bank=["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))  # 4
    print(s.minMutation(startGene="AAAACCCC", endGene="CCCCCCCC",
          bank=["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"]))  # 4
