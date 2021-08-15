# 素数

## 約数列挙

$O(\sqrt{N})$ で約数を列挙

一応リストにして返している

```python
def divisors(N: int):
    '''
    約数列挙
    O(N**0.5)
    sort しなくて良い場合は調整する
    '''
    divisors = set()
    i = 1
    while i*i <= N:
        if N % i == 0:
            divisors.add(i)
            divisors.add(N//i)
        i += 1
    return sorted(list(divisors))
```


## 素因数分解

### 試し割り法 Trial division

$O(\sqrt{N})$


```python
class PrimeFactorize:
    def __init__(self, N: int):
        '''
        N を素因数分解
        '''
        self.primes = []
        n = N

        # よくある高速化
        # 偶数を落としておく
        while n % 2 == 0:
            n //= 2
            self.primes.append(2)

        div = 3
        while div*div <= n:
            while n % div == 0:
                self.primes.append(div)
                n //= div
            div += 2

        if n != 1:
            self.primes.append(n)

    def get_counts(self):
        '''
        dict で返す
        '''
        import collections
        return dict(collections.Counter(self.primes))
```


### エラトステネスの篩

$O(N \log \log N)$ で素数判定用のリストを返す

```python
def sieve(n):
    '''
    エラトステネスの篩
    O(N log log N)
    '''
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n+1):
        if is_prime[i]:
            j = i + i
            while j <= n:
                is_prime[j] = False
                j += i
    return is_prime

```
### 高速素因数分解

$O(N \log N)$ で初期化

$O(\log N)$ で素因数分解

```python
class SmallestPrimeFactors:
    '''
    高速素因数分解
    最小の素数を返す
    O(N log N)
    '''

    def __init__(self, N: int):
        table = [i for i in range(N+1)]
        i = 2
        while i*i <= N:
            # 素数の場合
            if table[i] == i:
                j = i
                while j <= N:
                    if table[j] == j:
                        table[j] = i
                    j += i
            i += 1
        self._table = table

    def prime_factorize(self, N: int):
        factors = []
        n = N
        while n > 1:
            factor = self._table[n]
            n //= factor
            factors.append(factor)
        return factors

```