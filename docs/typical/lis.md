# LIS

最長増加部分列を求める

```python
def lis(A):
    '''
    最長増加部分列(LIS)
    '''
    from bisect import *

    INF = 10**10
    N = len(A)
    dp = [INF]*(N+1)
    dp[0] = -1
    # dp[i] := 長さが i の列で最後が dp[i] のやつ
    for a in A:
        ind = bisect_left(dp, a)
        dp[ind] = min(a, dp[ind])

    return max(i for i in range(N+1) if dp[i] < INF)
```

以下のパターンもある
```python
ind = bisect(dp, a-1)
```
