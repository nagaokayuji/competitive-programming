# Rolling Hash

```python
class RollingHash():
    def __init__(self, s: str, base=10007, mod=2**61 - 1):
        n = len(s)
        self.mod = mod
        self.hash = hash = [0]*(n+1)
        self.pw = pw = [1]*(len(s)+1)

        for i in range(n):
            pw[i+1] = pw[i] * base % mod

        for i in range(n):
            hash[i+1] = (hash[i] * base + ord(s[i])) % mod

    def get(self, l: int, r: int):
        '''
        get hash of [l,r)  (0-indexed)
        '''
        return (self.hash[r] - self.hash[l] * self.pw[r-l]) % self.mod
```

### example
```python
rh = RollingHash("hogehogestring")
assert(rh.get(0, 1) == rh.get(4, 5))
assert(rh.get(0, 2) == rh.get(4, 6))
assert(rh.get(0, 3) == rh.get(4, 7))
assert(rh.get(0, 4) == rh.get(4, 8))
```