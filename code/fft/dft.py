import numpy as np
import math


def dft(a, reverse=False):
    n = len(a)
    b = [complex()]*n

    sign = -1 if reverse else 1
    for i in range(n):
        for j in range(n):
            b[i] += a[j] * np.exp(complex(0, sign * i * j * 2 * math.pi / n))
        if reverse:
            b[i] /= n
    return b


lst = [1+1j, 2+1j, 5+5j, 4+0j]

fft = dft(lst)
rfft = dft(fft, True)

print(lst)
print(fft)
print(rfft)
