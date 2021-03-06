# Fenwick Tree (BIT)

長さNのリストにおいて、

1点加算（変更）、区間和取得 を $O(\log N)$ で行うことができる。

以下の実装では `0-indexed`

### コピー用実装

```python
class FenwickTree:
    def __init__(self, n: int = 10**6):
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x):
        p += 1
        while p <= self._n:
            self.data[p-1] += x
            p += p & -p

    def sum(self, left: int, right: int):
        return self._sum(right) - self._sum(left)

    def _sum(self, r: int):
        s = 0
        while r > 0:
            s += self.data[r-1]
            r -= r & -r
        return s
```