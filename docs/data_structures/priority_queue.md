# Priority Queue

`heapq` を使用する。 [公式ドキュメント](https://docs.python.org/ja/3/library/heapq.html)

デフォルトで昇順のため Rust と逆。

使用する場合は import する。


## import
```python
from heapq import *
```

## 作成
適当なリストを heapq に変換

```python
l = [1,0,-1,3]
heapify(l)
```

## l から先頭を取り出す

```python
heappop(l)
```

## l に 要素を追加

```python
heappush(l, 123)
```


## 最大値を取り出したい場合

符号を反転して突っ込むのが楽そう


## 例

- [ABC141 D - Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d)

最大値取り出し

```python
from heapq import *


N, M = map(int, input().split())

A = list(map(int, input().split()))

pq = []

for x in A:
    heappush(pq, -x)

for _ in range(M):
    val = -heappop(pq)
    heappush(pq, -(val//2))

print(-sum(pq))
```