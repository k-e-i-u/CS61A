from operator import mul
import pysnooper
from icecream import ic
# 结合高阶函数higher-order function应用python list的例子。

# 传入一个函数作为映射函数。
# 对一个python list应用list comprehension.
# 最终得到基于原列表s的一个函数map_fn映射后的新列表。
def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

# 传入一个函数作为过滤函数。
# 对一个python list应用list comprehension.
# 最终得到基于原列表s的一个函数filter_fn过滤后的子列表。
def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

# 结合高阶函数特性，实现reduce list的功能。
# reduce就是将一个函数应用到一个列表的每个元素上，
# 最后根据计算，只能返回一个值。
@pysnooper.snoop()
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

reduce(mul, [2, 4, 8], 1)


# 最后时利用reduce函数
# 实现计算perfect number
# 完美数的定义是：一个数等于它的所有真因子之和。
# 常见完美数有：1，6, 28, 496, 8128
# 例如：6 = 1 + 2 + 3
# 28 = 1 + 2 + 4 + 7 + 14
def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

from operator import add
def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

ic(keep_if(perfect, range(1, 1000)))