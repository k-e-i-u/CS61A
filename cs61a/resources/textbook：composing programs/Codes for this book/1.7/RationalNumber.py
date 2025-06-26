import pysnooper
import math
# A rational number is a ratio of integers, and rational numbers 
# constitute an important sub-class of real numbers. A rational 
# number such as 1/3 or 17/29 is typically written as: <numerator>/<denominator>
# （1）我们在开发时，同样可以使用经典的假设开发法（WISHFUL THINKING）。
#  我们假设现在已经实现好了三个函数，功能分别为：
#  rational(numerator, denominator) 可以传入一个分子和一个分母，返回一个有理数对象。
#  numer(x) 可以传入一个有理数对象，返回它的分子。
#  denom(x) 可以传入一个有理数对象，返回它的分母。
#  这三个函数的实现都不需要我们关心，我们先假设它们都开发好了，且能正常使用。
#  然后我们就可以使用这三个函数，先来实现有理数的加法、乘法、相等判断、打印等操作。
## def rational(numerator, denominator):
##     pass
## def numer(x):
##     pass
## def denom(x):
##     pass

@pysnooper.snoop()
def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

@pysnooper.snoop()
def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

@pysnooper.snoop()
def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

# 设置一个默认参数，当有需要按照最小项打印时，传入True即可。
# 这里我们使用了一个默认参数gcd，默认为False，表示不需要最小项打印。
@pysnooper.snoop()
def print_rational(x, gcd=False):
    if gcd:
        x = rational_gcd(numer(x), denom(x))
    print('当前有理数打印是：', numer(x), '/', denom(x))

# （2）我们可以使用一个列表来表示有理数对象，列表的第一个元素是分子，第二个元素是分母。
#  这样我们就可以实现上面三个函数了。

# 普通列表版本的有理数函数
@pysnooper.snoop()
def rational(n, d):
    return [n, d]

# 自动最小项版本的有理数函数
@pysnooper.snoop()
def rational_gcd(n, d):
    g = math.gcd(n, d)
    return (n//g, d//g)

@pysnooper.snoop()
def numer(x):
    return x[0]

@pysnooper.snoop()
def denom(x):
    return x[1]


def main():
    """Main function to test all debugging methods."""
    try:
        half = rational(1, 2)
        print_rational(half)
        third = rational(1, 3)
        print_rational(mul_rationals(half, third))
        print_rational(add_rationals(third, third), True)  
    except AssertionError as e:
        print(f"Error: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()