# dijkstra
## requirements
`from heapq import heappush, heappop`
- `g: 隣接リスト`
- `start: 始点`
- `return: startからの最短距離リスト`
## code

```python
def dijkstra(g, start):
    dists = [10**18] * N
    dists[start] = 0
    que = [(0, start)]
    while que:
        p = heappop(que)
        c = p[0]
        v = p[1]
        if dists[v] < c:
            continue
        for to, cost in g[v]:
            if dists[to] > dists[v] + cost:
                dists[to] = dists[v] + cost
                heappush(que, (dists[to], to))
    return dists
```

参考: 蟻本 pp.96 - 97