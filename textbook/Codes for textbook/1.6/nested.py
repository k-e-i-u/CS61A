def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

# 配套sqrt_update的函数。
def average(x, y):
    return (x + y)/2

# 这个update函数，明显不适用于improve函数，其update参数绑定的
# 传入函数，仅接受一个参数，而sqrt_update函数需要传入两个参数。
def sqrt_update(x, a):
    return average(x, a/x)

# 此时的sqrt_update需要传入两个参数才可以用。
# 明显和improve函数不配套、不适用。
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

# 为了使用improve，我们只能用nested function的特性
# 在sqrt_update函数的外面，再包装一层函数，用来接收参数a
# 此时的sqrt_update函数就只需要接受一个参数了。
# sqrt_close函数也同理。
def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

