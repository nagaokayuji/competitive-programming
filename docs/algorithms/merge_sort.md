# マージソート

再帰で実装する。

$O(N \log N)$

## コード
```python
def merge(a, b):
    aind = 0
    bind = 0
    na = len(a)
    nb = len(b)
    ret = []
    while aind < na and bind < nb:
        if a[aind] <= b[bind]:
            ret.append(a[aind])
            aind += 1
        else:
            ret.append(b[bind])
            bind += 1
    if aind < na:
        ret += a[aind:]
    else:
        ret += b[bind:]
    return ret

def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    a = lst[0:n//2]
    b = lst[n//2:]

    return merge(merge_sort(a), merge_sort(b))
```