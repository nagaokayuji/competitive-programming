# ユークリッドの互除法

最大公約数 $gcd(a,b)$ を高速に求める。

自明な性質として、
$gcd(0,x) = x$、$gcd(1,x) = 1$ がある。

$gcd(a,b) = gcd(b, a\%b)$ が成り立つ。 

実は Python の場合は `math` をimport して使用できるため、実装する必要はない。
```python
import math
math.gcd(a,b)
```

## 拡張ユークリッドの互除法

$a\cdot x + b\cdot y = gcd(a,b)$ となる $x,y$ を求めることができる。

ユークリッドの互除法より、左辺は

$$
(b \% a) \cdot x_1 + a \cdot y_1
$$

とおける。

このとき、両辺に$x_1$を掛けて
$$
(b \% a ) \cdot x_1 + (b/a) \cdot a \cdot x_1 = b \cdot x_1
$$
移項して
$$
(b \% a) \cdot x_1 = b \cdot x_1 - (b/a) \cdot a \cdot x_1
$$



一般に、

$$
\left\{
\begin{aligned}
a_{k+1} &= b_k \\
b_{k+1} &= a_k \% b_k
\end{aligned}
\right.
$$

として

$$
\begin{aligned}
a_k \cdot x_k +  b_k \cdot y_k &= b_k \cdot x_{k+1} + (a_k\% b_k) \cdot y_{k+1} \\ &= a_{k+1} \cdot x_{k+1} + b_{k+1} \cdot y_{k+1}
\end{aligned}
$$
と変形していき

最終的に $0 \cdot x_n + b_n\cdot y_n = gcd(a,b)$ が得られたとすると、




$$
\left\{
\begin{aligned}
x_{k-1} &= y_k + (b_{k-1}/a_{k-1}) \cdot x_k \\
y_{k-1} &= x_k
\end{aligned}
\right.
$$
を利用して
元の$x,y$を求めることができる。
