import numpy as np
f = np.array([1, 2, 6, 4, -2])
g = np.array([8, 15, 5, 2])
fft_len = 16

Ff = np.fft.rfft(f, fft_len)
print(Ff)
Fg = np.fft.rfft(g, fft_len)
print(Fg)

Ffg = Ff * Fg
print(Ffg)

fg = np.fft.irfft(Ffg, fft_len)
fg = np.rint(fg)
print(fg)

lst = [1, 2, 34, 4, 6, 7, 7, 78, 12, -1]


f = np.fft.rfft(lst)

print(f)
rv = np.fft.irfft(f)
print(np.rint(rv))
