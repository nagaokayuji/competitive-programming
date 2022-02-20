# Z-Algorithm

## Z-Algorithm とは？

文字列Sが与えられる。

このとき、`Z[i] = S と S[i:] の共通接頭辞の長さ(Longest Common Prefix, LCP)` となるリスト `Z` がほしい。


これを $O(N)$ で生成する。

※ 入力 S の長さを N とすると、
Z[0] = N は明らかに成立する。

## コード
```python
import typing


def z_algorithm(s: typing.Union[str, typing.List[int]]) -> typing.List[int]:
    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)
    if n == 0:
        return []

    z = [0] * n
    last = 0
    for i in range(1, n):
        last_ind = last + z[last]
        now = 0 if last_ind <= i else min(last_ind - i, z[i - last])

        while i + now < n and s[now] == s[i + now]:
            now += 1

        if last_ind < i + now:
            last = i

        z[i] = now

    z[0] = n
   return z
```



## メモ

- 基本的に左からみていく
- どこまで比較したかを記録

### 愚直な実装$O(N^2)$

```python
def z_algorithm_naive(s):
    '''
    s: str または list
    愚直な実装
    O(N^2)
    '''
    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)
    if n == 0:
        return []

    z = [0] * n
    z[0] = n

    for i in range(1, n):
        now = z[i]
        while i + now < n and s[now] == s[i + now]:
            now += 1
        z[i] = now

    return z
```
