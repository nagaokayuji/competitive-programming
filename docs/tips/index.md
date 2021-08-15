# tips

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
sys.setrecursionlimit(10**6)
```