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
