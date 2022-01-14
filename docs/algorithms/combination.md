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

```python
class ModComb:
    def __init__(self, N=10**6, MOD=10**9 + 7):
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
        if n < k or n < 0 or k < 0:
            return 0
        return (self.factorial[n] * self.inv_factorial[k] % self.MOD) * self.inv_factorial[n-k] % self.MOD

    def comb_multi(self, n, k):
        return self.comb(n+k-1, k)
```