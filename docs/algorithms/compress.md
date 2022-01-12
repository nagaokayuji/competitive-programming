# 座標圧縮

## 一次元リスト

あまり早くない

```python
def compress(A):
    d = {v: i for i, v in enumerate(sorted(set(A)))}
    return list(map(lambda x: d[x], A))
```

### example
```python
A = [-123, 23, 0, 1000, 56]
print(compress(A))  # [0, 2, 1, 4, 3]
```