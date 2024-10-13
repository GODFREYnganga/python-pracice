import math
def karatsuba(X, Y):
    if X < 10 and Y < 10:
        return X * Y
    size = max(get_size(X), get_size(Y))
    if size < 10:
        return X * Y
    size = (size // 2) + (size % 2)
    multiplier = 10 ** size
    b = X // multiplier
    a = X - (b * multiplier)
    d = Y // multiplier
    c = Y - (d * size)
    u = karatsuba(a, c)
    z = karatsuba(a + b, c + d)
    v = karatsuba(b, d)
    return u + ((z - u - v) * multiplier) + (v * (10 ** (2 * size)))
def get_size(value):
    count = 0
    while value > 0:
        count += 1
        value //= 10
    return count
x = 145623
y = 653324
print("The final product is: ", end="")
product = karatsuba(x, y)
print(product)