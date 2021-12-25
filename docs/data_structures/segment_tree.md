# Segment Tree

## code
```python
class SegmentTree:
    def __init__(self, n: int, initial: any, op):
        m = 1
        while m <= (n+1):
            m *= 2

        self.m = m
        self.array = [initial] * (2*m)
        self.op = op
        self.initial = initial

    def update(self, index: int, val: any):
        pos = self.m + index
        self.array[pos] = val  # update
        while pos > 1:  # update forward root
            pos >>= 1
            self.array[pos] = self.op(self.array[pos*2], self.array[pos*2+1])

    def add(self, index: int, val: any):
        self.update(index, self.array[self.m+index]+val)

    def get(self, l: int, r: int):
        '''
        get value of [l,r)
        '''
        assert(l < r)
        ret = self.initial
        l += self.m
        r += self.m
        while l < r:
            if l % 2 == 1:
                ret = self.op(ret, self.array[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                ret = self.op(ret, self.array[r-1])
                r -= 1
            r //= 2
        return ret
```

## example
- range sum query

```python

def op(a, b):
    return a+b


seg = SegmentTree(N, 0, op)
for i, x in enumerate(a):
    seg.update(i, x)

for _ in range(Q):
    t, a, b = mi()
    if t == 0:
        seg.add(a, b)
    else:
        print(seg.get(a, b))
```
