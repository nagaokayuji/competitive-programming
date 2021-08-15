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
