class FenwickTree:
    '''
    Fenwick Tree (BIT)
    '''

    def __init__(self, n: int = 0):
        '''
        長さnで初期化
        '''
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x):
        '''
        x を加算
        '''
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int):
        '''
        [l, r) の和を取得
        '''
        return self._sum(right) - self._sum(left)

    def _sum(self, r: int):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


N, Q = map(int, input().split())
a = list(map(int, input().split()))
bit = FenwickTree(N)
ans = []
for i, x in enumerate(a):
    bit.add(i, x)
for _ in range(Q):
    _a, _b, _c = map(int, input().split())
    if _a == 0:
        bit.add(_b, _c)
    else:
        ans.append(bit.sum(_b, _c))

print(*ans)
