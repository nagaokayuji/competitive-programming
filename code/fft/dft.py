import numpy as np
import math


def dft(a, reverse=False):
    n = len(a)
    b = [complex()]*n

    sign = -1 if reverse else 1
    for i in range(n):
        for j in range(n):
            b[i] += a[j] * np.exp(complex(0, sign * i * j * 2 * math.pi / n))
    return b


def fft(a, reverse=False):
    ret = a.copy()
    n = len(a)
    if n == 1:
        return a
    b = fft(a[0:n:2], reverse)
    c = fft(a[1:n:2], reverse)
    circle = 2 * math.pi * -1 if reverse else 1
    for i in range(n):
        ret[i] = b[i % (n//2)] + c[i % (n//2)] * np.exp(complex(0, circle*i/n))
    return ret
