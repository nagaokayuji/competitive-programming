# tips

Python 特有の tips

## 入力を高速に受け取る
`input()` で遅い場合は以下を検討

```python
import sys
stdin = sys.stdin
 
rd = lambda: stdin.readline().strip()
ri = lambda: int(ns())
ril = lambda: list(map(int, stdin.readline().split()))
```

## print() 関数を何度も呼ばない

以下は遅い

```python
for i in range(n):
    print(solve(i))
```

例えば、以下のようにするとマシになる。

```python
ans = []
for i in range(n):
    ans.append(sole(i))

print(*ans)
```

## defaultdict を使うと便利

デフォルト値を指定できる。

```python
from collections import defaultdict

dct = defaultdict(int)

for x in arr:
    dct[x] += 1
```

`list` の場合
```python
dct = defaultdict(list)
for x,y in arr:
    dct[x].append(y)
```

初期値を変えたい場合
```python
dct = defaultdict(lambda: 10)
```


## deque を使う

`deque` を使うと高機能。
スタック/キューとして使える。

```python
from collections import deque
```

## 再帰を深くする

DFS などをするときは以下を追加

```python
import sys
sys.setrecursionlimit(10**8)
```

## リストの代わりに dict を使う

3重配列などを宣言するのは面倒なため、
特に defaultdict と組み合わせると実装が楽になる。

Python では tuple をキーに取れることを利用して以下のように書ける。

```python
from collections import defaultdict

dp = defaultdict(int)
dp[0,0,0] = 1
```

## リストの代わりに array を使う

`list` を少し速くしたい場合に便利。

リストとほぼ同じように扱える。


```python
import array

l = array.array("i", []) # int 型の array
```

[array --- 効率のよい数値アレイ — Python 3.9.4 ドキュメント](https://docs.python.org/ja/3/library/array.html)


## 90度回転

```python
def rot(s):
    '''
    二次元配列を90度回転
    '''
    return list(zip(*s[::-1])
```

## 座標圧縮
```python
def compress(A):
    '''
    座標圧縮
    compress([1, 2, 3, 123, 1, 3, 4, 61231, 1, 3]))
     → [0, 1, 2, 4, 0, 2, 3, 5, 0, 2]
    '''
    xmap = {x: i for i, x in enumerate(sorted(set(A)))}
    return list(map(lambda x: xmap[x], A))

```