# numba

## numbaとは？
jit(just in time) コンパイルを行えるライブラリ。


## 基本的な使い方

対象の関数に `@jit` をつける。

`@njit` とすると noPython モードとなり、高速化の際はこちらを使っておくと良さそう。
```python
import numba

@numba.njit
def some_function():
    pass

```

## 型を指定する


指定したほうが速いとのこと。

`@njit('返り値の型(引数の型)')`

```python
@njit('i8(i8[:])')
def func(array):
    return 合計
```

### 型をimport

文字列より安全そう。

```python
from numba import njit, f8, i8, b1, u8, c8
```

