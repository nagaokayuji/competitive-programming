# 二項係数

組み合わせを求める方法について述べる。

## 雑に計算したい場合

`math.comb()` で求められる。 
AtCoder で使用できる。

```python
import math
math.comb(4,2) # 6
```

## 前計算後に高速に求めたい場合

以下を参考に実装した。

[よくやる二項係数 (nCk mod. p)、逆元 (a^-1 mod. p) の求め方](https://drken1215.hatenablog.com/entry/2018/06/08/210000)

逆元リストを用いず、$N!$ の逆元を最初に求める方式を採用した。

また、重複組合せも求められるようにした。

```python
class ModComb:
    '''
    O(N) で初期化、O(1) でクエリ処理
    二項係数を求める
    '''

    def __init__(self, N=10**6, MOD=10**9 + 7):
        '''
        最大 N まで
        '''
        self.MOD = MOD
        self.N = N
        self.factorial = [1] * (N+1)

        for i in range(2, N+1):
            self.factorial[i] = self.factorial[i-1]*i % MOD

        self.inv_factorial = [1] * (N+1)
        # N! の逆元を先に計算
        self.inv_factorial[N] = pow(self.factorial[N], MOD-2, MOD)
        # (N-1)! / (N!) * N = 1
        for i in range(N, 1, -1):
            self.inv_factorial[i-1] = self.inv_factorial[i]*i % MOD

    def comb(self, n, k):
        '''
        二項係数 nCk
        '''
        if n < k or n < 0 or k < 0:
            return 0
        return (self.factorial[n] * self.inv_factorial[k] % self.MOD) * self.inv_factorial[n-k] % self.MOD

    def comb_multi(self, n, k):
        '''
        重複組合せ nHk
        '''
        return self.comb(n+k-1, k)
```