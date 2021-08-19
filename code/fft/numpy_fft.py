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
