# SCC

```python

sys.setrecursionlimit(1111111)


class SCC:
    def __init__(self, n: int):
        ''' n: num of nodes'''
        self.n = n
        self.g = [[] for _ in range(n)]
        self.rg = [[] for _ in range(n)]

    def from_graph(self, g: List[List[int]]):
        self.n = n = len(g)
        self.g = g.copy()
        self.rg = [[] for _ in range(n)]
        for v in range(n):
            for to in g[v]:
                self.rg[to].append(v)

    def add_edge(self, _from: int, to: int):
        self.g[_from].append(to)
        self.rg[to].append(_from)

    def scc(self):
        n = self.n
        group = [None] * n  # トポロジカル順序
        used = [False] * n
        order = []  # 帰りがけ順の並び

        def dfs(v: int):
            used[v] = True
            for nx in self.g[v]:
                if not used[nx]:
                    dfs(nx)
            order.append(v)

        def rdfs(v: int, group_label: int):
            used[v] = True
            group[v] = group_label
            for nx in self.rg[v]:
                if not used[nx]:
                    rdfs(nx, group_label)

        for v in range(n):
            if not used[v]:
                dfs(v)

        used = [False] * n
        group_label = 0

        for i in range(n-1, -1, -1):
            if not used[order[i]]:
                rdfs(order[i], group_label)
                group_label += 1

        return group_label, group

```