# Newton's method is an iterative improvement algorithm: 
# it improves a guess of the zero for any function that 
# is differentiable, which means that it can be approximated
# by a straight line at any point. 
# Newton's method follows these linear approximations to find function zeros.

# As you experiment with Newton's method, be aware that it will 
# not always converge. The initial guess of improve must be 
# sufficiently close to the zero, and various conditions about 
# the function must be met.

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

# The approximation error in all of these computations 
# can be reduced by changing the tolerance in approx_eq to a smaller number.
def approx_eq(x, y, tolerance=1e-16):
        return abs(x - y) < tolerance

# This line's slope is the ratio of the change in function value 
# to the change in function argument. Hence, translating x by f(x)
# divided by the slope will give the argument value at which this tangent line touches 0.
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

#这里的newton_update(f,df)(guess)就是一个currying的例子
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)   

# Using Newton's method, we can compute roots of arbitrary degree n.
# The square (second) root of 64 is 8, because 8⋅8=64
# The cube (third) root of 64 is 4, because 4⋅4⋅4=64
def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

print(square_root_newton(64))

# Generalizing to roots of arbitrary degree n
# we compute f(x)=xn−a
# and its derivative df(x)=n⋅xn−1
def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)

print(nth_root_of_a(2, 64))   # correct! 2^8 - 64 = 0