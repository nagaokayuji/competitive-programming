# 転倒数

求め方が複数ある。
どちらも計算量は$O(N \log N)$となる。

- BIT を用いる方法
- 分割統治法による方法

BIT を用いる方法の方が分かりやすいと思うが、今回は分割統治法による方法について載せる。

## 実装

```python
def inversions(a):
    count = 0
    n = len(a)
    if n >= 2:
        b = a[0:n//2].copy()
        c = a[n//2:n].copy()
        count += inversions(b) + inversions(c)

        # b,c は sort されている。
        # merge sort をしていく流れで count
        ai = bi = ci = 0
        while ai < n:
            if bi < len(b) and (ci == len(c) or b[bi] <= c[ci]):
                a[ai] = b[bi]
                bi += 1
            else:
                count += len(b) - bi
                a[ai] = c[ci]
                ci += 1
            ai += 1
    return count
```

### 注意点
渡したリストはソートされる。

### 分割

半分に分けて再帰的に呼び出していく。

```python
        b = a[0:n//2].copy()
        c = a[n//2:n].copy()
        count += inversions(b) + inversions(c)
```

### 統合

マージソートの要領でマージしていく。

リストBのうち、マージされていない要素の個数を足す。

```python
        ai = bi = ci = 0
        while ai < n:
            if bi < len(b) and (ci == len(c) or b[bi] <= c[ci]):
                a[ai] = b[bi]
                bi += 1
            else:
                count += len(b) - bi
                a[ai] = c[ci]
                ci += 1
            ai += 1
```
