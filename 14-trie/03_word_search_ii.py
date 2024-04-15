"""[[ HARD ]]"""
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

    # def __str__(self) -> str:
    #     return str(self.children)
    def insert(self, word: str) -> None:
        word_len = len(word)
        n = self
        for i in range(word_len):
            c = word[i]
            if c in n.children:
                if i == word_len - 1:
                    n.children[c].is_end_of_word = True
            else:
                n.children[c] = TrieNode()
                n.children[c].is_end_of_word = i == word_len - 1
            n = n.children[c]

    # def startsWith(self, prefix: str) -> bool:
    #     n = self.node
    #     for i in range(len(prefix)):
    #         idx = ord(prefix[i]) - ord('a')
    #         n = n.children[idx]
    #         if not n:
    #             return False
    #     return True

    # def search(self, word: str) -> bool:
    #     n = self.node
    #     word_len = len(word)
    #     for i in range(word_len):
    #         idx = ord(word[i]) - ord('a')
    #         n = n.children[idx]
    #         if not n or (i == word_len-1 and not n.is_end_of_word):
    #             return False
    #     return True

    # def remove(self, word: str) -> bool:
    #     if self.startsWith(word):
    #         n = self.node
    #         # x, last_end_node = 0, self.node
    #         word_len = len(word)
    #         nodes = []
    #         for i in range(word_len):
    #             idx = ord(word[i]) - ord('a')
    #             n = n.children[idx]
    #             nodes.append((idx, n))

    #         n = nodes[len(nodes) - 1]
    #         n[1].is_end_of_word = False
    #         # print('word =', word, 'nodes =', [(i, str(n)) for i, n in nodes])
    #         while nodes:
    #             i, n = nodes.pop()
    #             # print('i, n =', i, n)
    #             if n.is_end_of_word:
    #                 n.children[i] = None
    #                 break
    #             if len([i for i in range(26) if n.children[i]]) == 0:
    #                 n = nodes[-1][1] if nodes else self.node
    #                 # print('before', n.children[i])
    #                 n.children[i] = None
    #                 # print('after', n.children[i])
    #                 # n = None


class Solution:
    def _get_neighbors(self, board, pos, pos_history):
        row, col = pos
        result = []
        # top
        if row > 0 and (row-1, col) not in pos_history:
            result.append((row-1, col))
        # bottom
        if row < len(board)-1 and (row+1, col) not in pos_history:
            result.append((row+1, col))
        # left
        if col > 0 and (row, col-1) not in pos_history:
            result.append((row, col-1))
        # right
        if col < len(board[0])-1 and (row, col+1) not in pos_history:
            result.append((row, col+1))
        return result

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            trie.insert(w)
        # print(trie.children)
        result = set()
        pos_history = set()

        def _track(pos, word, node):
            if len(word) <= 10:
                c = word[-1]
                # print('c, node =', c, node.children)
                if not node or c not in node.children:
                    return
                if node.children[c].is_end_of_word:
                    result.add(''.join(word))

                pos_history.add(pos)
                neighbors = self._get_neighbors(board, pos, pos_history)
                # print('neighbors =', neighbors)
                for p in neighbors:
                    n = board[p[0]][p[1]]
                    # if n in node.children[c]:
                    word.append(n)
                    _track(p, word, node.children[c])
                    word.pop()
                pos_history.remove(pos)

        for i in range(len(board)):
            for j in range(len(board[0])):
                _track((i, j), [board[i][j]], trie)
        return list(result)


if __name__ == '__main__':
    s = Solution()
    print(
        s.findWords(
            board=[["o", "a", "a", "n"],
                   ["e", "t", "a", "e"],
                   ["i", "h", "k", "r"],
                   ["i", "f", "l", "v"]],
            words=["oath", "pea", "eat", "rain"]
        )
    )  # ['oath', 'eat']
    print(s.findWords(board=[["a"]], words=["a"]))  # ['a']
    print(s.findWords([
        ["o", "a", "b", "n"],
        ["o", "t", "a", "e"],
        ["a", "h", "k", "r"],
        ["a", "f", "l", "v"]],
        ["oa", "oaa"]
    ))  # ['a']
    print(s.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))  # []
    print(s.findWords([
        ["c", "c", "c", "a", "c", "b", "d", "a", "d"],
        ["b", "e", "a", "e", "e", "c", "a", "c", "b"],
        ["b", "c", "a", "d", "a", "c", "e", "d", "a"],
        ["c", "c", "c", "a", "b", "c", "a", "a", "d"],
        ["d", "d", "a", "d", "e", "e", "e", "c", "a"],
        ["e", "e", "b", "a", "d", "a", "a", "e", "c"],
        ["a", "a", "d", "a", "c", "c", "e", "a", "d"],
        ["e", "d", "b", "e", "b", "d", "e", "e", "c"],
        ["c", "a", "a", "a", "c", "a", "e", "b", "d"],
        ["a", "b", "e", "b", "b", "d", "e", "c", "c"],
        ["a", "e", "d", "e", "c", "c", "e", "e", "a"]
    ], ["addeddeabb"]))  # []
    print(
        s.findWords(
            board=[
                ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
                ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
                ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
                ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
                ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
                ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
                ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
                ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
                ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"],
                ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]
            ],
            words=["ababababaa", "ababababab", "ababababac",
                   "ababababad", "ababababae", "ababababaf", "ababababag",
                   "ababababah", "ababababai", "ababababaj", "ababababak", "ababababal", "ababababam", "ababababan",
                   "ababababao", "ababababap", "ababababaq", "ababababar", "ababababas", "ababababat", "ababababau",
                   "ababababav", "ababababaw", "ababababax", "ababababay", "ababababaz", "ababababba", "ababababbb",
                   "ababababbc", "ababababbd", "ababababbe", "ababababbf", "ababababbg", "ababababbh", "ababababbi",
                   "ababababbj", "ababababbk", "ababababbl", "ababababbm", "ababababbn", "ababababbo", "ababababbp",
                   "ababababbq", "ababababbr", "ababababbs", "ababababbt", "ababababbu", "ababababbv", "ababababbw",
                   "ababababbx", "ababababby", "ababababbz", "ababababca", "ababababcb", "ababababcc", "ababababcd",

                   "ababababce", "ababababcf", "ababababcg", "ababababch", "ababababci", "ababababcj", "ababababck",
                   "ababababcl", "ababababcm", "ababababcn", "ababababco", "ababababcp", "ababababcq", "ababababcr",
                   "ababababcs", "ababababct", "ababababcu", "ababababcv", "ababababcw", "ababababcx", "ababababcy",
                   "ababababcz", "ababababda", "ababababdb", "ababababdc", "ababababdd", "ababababde", "ababababdf",
                   "ababababdg", "ababababdh", "ababababdi", "ababababdj", "ababababdk", "ababababdl", "ababababdm",
                   "ababababdn", "ababababdo", "ababababdp", "ababababdq", "ababababdr", "ababababds", "ababababdt",
                   "ababababdu", "ababababdv", "ababababdw", "ababababdx", "ababababdy", "ababababdz", "ababababea",
                   "ababababeb", "ababababec", "ababababed", "ababababee", "ababababef", "ababababeg", "ababababeh",
                   "ababababei", "ababababej", "ababababek", "ababababel", "ababababem", "ababababen", "ababababeo",
                   "ababababep", "ababababeq", "ababababer", "ababababes", "ababababet", "ababababeu", "ababababev",
                   "ababababew", "ababababex", "ababababey", "ababababez", "ababababfa", "ababababfb", "ababababfc",
                   "ababababfd", "ababababfe", "ababababff", "ababababfg", "ababababfh", "ababababfi", "ababababfj",
                   "ababababfk", "ababababfl", "ababababfm", "ababababfn", "ababababfo", "ababababfp", "ababababfq",
                   "ababababfr", "ababababfs", "ababababft", "ababababfu", "ababababfv", "ababababfw", "ababababfx",
                   "ababababfy", "ababababfz", "ababababga", "ababababgb", "ababababgc", "ababababgd", "ababababge",
                   "ababababgf", "ababababgg", "ababababgh", "ababababgi", "ababababgj", "ababababgk", "ababababgl",
                   "ababababgm", "ababababgn", "ababababgo", "ababababgp", "ababababgq", "ababababgr", "ababababgs",
                   "ababababgt", "ababababgu", "ababababgv", "ababababgw", "ababababgx", "ababababgy", "ababababgz",
                   "ababababha", "ababababhb", "ababababhc", "ababababhd", "ababababhe", "ababababhf", "ababababhg",
                   "ababababhh", "ababababhi", "ababababhj", "ababababhk", "ababababhl", "ababababhm", "ababababhn",
                   "ababababho", "ababababhp", "ababababhq", "ababababhr", "ababababhs", "ababababht", "ababababhu",
                   "ababababhv", "ababababhw", "ababababhx", "ababababhy", "ababababhz", "ababababia", "ababababib",
                   "ababababic", "ababababid", "ababababie", "ababababif", "ababababig", "ababababih", "ababababii",
                   "ababababij", "ababababik", "ababababil", "ababababim", "ababababin", "ababababio", "ababababip",
                   "ababababiq", "ababababir", "ababababis", "ababababit", "ababababiu", "ababababiv", "ababababiw",

                   "ababababix", "ababababiy", "ababababiz", "ababababja", "ababababjb", "ababababjc", "ababababjd",
                   "ababababje", "ababababjf", "ababababjg", "ababababjh", "ababababji", "ababababjj", "ababababjk",
                   "ababababjl", "ababababjm", "ababababjn", "ababababjo", "ababababjp", "ababababjq", "ababababjr",
                   "ababababjs", "ababababjt", "ababababju", "ababababjv", "ababababjw", "ababababjx", "ababababjy",
                   "ababababjz", "ababababka", "ababababkb", "ababababkc", "ababababkd", "ababababke", "ababababkf",
                   "ababababkg", "ababababkh", "ababababki", "ababababkj", "ababababkk", "ababababkl", "ababababkm", "ababababkn", "ababababko", "ababababkp", "ababababkq", "ababababkr", "ababababks", "ababababkt", "ababababku", "ababababkv", "ababababkw", "ababababkx", "ababababky", "ababababkz", "ababababla", "abababablb", "abababablc", "ababababld", "abababable", "abababablf", "abababablg", "abababablh", "ababababli", "abababablj", "abababablk", "ababababll", "abababablm", "ababababln", "abababablo", "abababablp", "abababablq", "abababablr", "ababababls", "abababablt", "abababablu", "abababablv", "abababablw", "abababablx", "abababably", "abababablz", "ababababma", "ababababmb", "ababababmc", "ababababmd", "ababababme", "ababababmf", "ababababmg", "ababababmh", "ababababmi", "ababababmj", "ababababmk", "ababababml", "ababababmm", "ababababmn", "ababababmo", "ababababmp", "ababababmq", "ababababmr", "ababababms", "ababababmt", "ababababmu", "ababababmv", "ababababmw", "ababababmx", "ababababmy", "ababababmz", "ababababna", "ababababnb", "ababababnc", "ababababnd", "ababababne", "ababababnf", "ababababng", "ababababnh", "ababababni", "ababababnj", "ababababnk", "ababababnl", "ababababnm", "ababababnn", "ababababno", "ababababnp", "ababababnq", "ababababnr", "ababababns", "ababababnt", "ababababnu", "ababababnv", "ababababnw", "ababababnx", "ababababny", "ababababnz", "ababababoa", "ababababob", "ababababoc", "ababababod", "ababababoe", "ababababof", "ababababog", "ababababoh", "ababababoi", "ababababoj", "ababababok", "ababababol", "ababababom", "ababababon", "ababababoo", "ababababop", "ababababoq", "ababababor", "ababababos", "ababababot", "ababababou", "ababababov", "ababababow", "ababababox", "ababababoy", "ababababoz", "ababababpa", "ababababpb", "ababababpc", "ababababpd", "ababababpe", "ababababpf", "ababababpg", "ababababph", "ababababpi", "ababababpj", "ababababpk", "ababababpl", "ababababpm", "ababababpn", "ababababpo", "ababababpp", "ababababpq", "ababababpr", "ababababps", "ababababpt", "ababababpu", "ababababpv", "ababababpw", "ababababpx", "ababababpy", "ababababpz", "ababababqa", "ababababqb", "ababababqc", "ababababqd", "ababababqe", "ababababqf", "ababababqg", "ababababqh", "ababababqi", "ababababqj", "ababababqk", "ababababql", "ababababqm", "ababababqn", "ababababqo", "ababababqp", "ababababqq", "ababababqr", "ababababqs", "ababababqt", "ababababqu", "ababababqv", "ababababqw", "ababababqx", "ababababqy", "ababababqz", "ababababra", "ababababrb", "ababababrc", "ababababrd", "ababababre", "ababababrf", "ababababrg", "ababababrh", "ababababri", "ababababrj", "ababababrk", "ababababrl", "ababababrm", "ababababrn", "ababababro", "ababababrp", "ababababrq", "ababababrr", "ababababrs", "ababababrt", "ababababru", "ababababrv", "ababababrw", "ababababrx", "ababababry", "ababababrz", "ababababsa", "ababababsb", "ababababsc", "ababababsd", "ababababse", "ababababsf", "ababababsg", "ababababsh", "ababababsi", "ababababsj", "ababababsk", "ababababsl", "ababababsm", "ababababsn", "ababababso", "ababababsp", "ababababsq", "ababababsr", "ababababss", "ababababst", "ababababsu", "ababababsv", "ababababsw", "ababababsx", "ababababsy", "ababababsz", "ababababta", "ababababtb", "ababababtc", "ababababtd", "ababababte", "ababababtf", "ababababtg", "ababababth", "ababababti", "ababababtj", "ababababtk", "ababababtl", "ababababtm", "ababababtn", "ababababto", "ababababtp", "ababababtq", "ababababtr", "ababababts", "ababababtt", "ababababtu", "ababababtv", "ababababtw", "ababababtx", "ababababty", "ababababtz", "ababababua", "ababababub", "ababababuc", "ababababud", "ababababue", "ababababuf", "ababababug", "ababababuh", "ababababui", "ababababuj", "ababababuk", "ababababul", "ababababum", "ababababun", "ababababuo", "ababababup", "ababababuq", "ababababur", "ababababus", "ababababut", "ababababuu", "ababababuv", "ababababuw", "ababababux", "ababababuy", "ababababuz", "ababababva", "ababababvb", "ababababvc", "ababababvd", "ababababve", "ababababvf", "ababababvg", "ababababvh", "ababababvi", "ababababvj", "ababababvk", "ababababvl", "ababababvm", "ababababvn", "ababababvo", "ababababvp", "ababababvq", "ababababvr", "ababababvs", "ababababvt", "ababababvu", "ababababvv", "ababababvw", "ababababvx", "ababababvy", "ababababvz", "ababababwa", "ababababwb", "ababababwc", "ababababwd", "ababababwe", "ababababwf", "ababababwg", "ababababwh", "ababababwi", "ababababwj", "ababababwk", "ababababwl", "ababababwm", "ababababwn", "ababababwo", "ababababwp", "ababababwq", "ababababwr", "ababababws", "ababababwt", "ababababwu", "ababababwv", "ababababww", "ababababwx", "ababababwy", "ababababwz", "ababababxa", "ababababxb", "ababababxc", "ababababxd", "ababababxe", "ababababxf", "ababababxg", "ababababxh", "ababababxi", "ababababxj", "ababababxk", "ababababxl", "ababababxm", "ababababxn", "ababababxo", "ababababxp", "ababababxq", "ababababxr", "ababababxs", "ababababxt", "ababababxu", "ababababxv", "ababababxw", "ababababxx", "ababababxy", "ababababxz", "ababababya", "ababababyb", "ababababyc", "ababababyd", "ababababye", "ababababyf", "ababababyg", "ababababyh", "ababababyi", "ababababyj", "ababababyk", "ababababyl", "ababababym", "ababababyn", "ababababyo", "ababababyp", "ababababyq", "ababababyr", "ababababys", "ababababyt", "ababababyu", "ababababyv", "ababababyw", "ababababyx", "ababababyy", "ababababyz", "ababababza", "ababababzb", "ababababzc", "ababababzd", "ababababze", "ababababzf", "ababababzg", "ababababzh", "ababababzi", "ababababzj", "ababababzk", "ababababzl", "ababababzm", "ababababzn", "ababababzo", "ababababzp", "ababababzq", "ababababzr", "ababababzs", "ababababzt", "ababababzu", "ababababzv", "ababababzw", "ababababzx", "ababababzy", "ababababzz"]
        )
    )
