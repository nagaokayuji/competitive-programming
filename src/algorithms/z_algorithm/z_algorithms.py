import typing


def z_algorithm(s: typing.Union[str, typing.List[int]]) -> typing.List[int]:
    '''
    s: str または list
    O(N)
    参考: https://github.com/not522/ac-library-python/blob/master/atcoder/string.py
    '''
    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)
    if n == 0:
        return []

    z = [0] * n

    # 一番うしろまで行ったやつの始点
    # 終点は (last + z[last]) でとれる
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


def z_algorithm_naive(s):
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


s = input()

z = z_algorithm(s)

print(*z)
