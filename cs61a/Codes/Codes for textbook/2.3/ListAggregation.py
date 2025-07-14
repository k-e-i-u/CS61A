# python list可以使用max, sum, min等聚合函数做聚合计算
import pysnooper
from icecream import ic

# 给定一个数n，计算可以整除n的，从1到n间的所有正整数。
def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

# 高阶函数版本的divisors函数。
# 将divisors函数通用判断逻辑的list comphrension
# 抽象出来，单独构建了keep_if函数，接收一个函数作为
# 过滤判断条件。
def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def divisors_hiorder(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

# 测试两个函数是否一致
ic(divisors(12))
ic(divisors_hiorder(12))

# 这里做聚合计算的测试，使用sum
[n for n in range(1, 1000) if sum(divisors(n)) == n]


# 利用list comphrehension和list aggregation特性
# 下面的一组代码，计算一个给定矩形的area，求边长为整数的最小周长。

# 计算矩形的宽
# 实际上divisors函数就已经能够保障area可以被height整除了。
# 但是为了其他代码调用width时的安全性，这里还是加上了assert语句，
# 确保area可以被height整除。
@pysnooper.snoop()
def width(area, height):
    assert area % height == 0  # 确保area可以被height整除，此时width也会为整数
    result = area // height
    return result

# 计算矩形的周长
def perimeter(width, height):
    result = 2 * width + 2 * height
    return result

# 通过divisors函数，计算一个给area的矩形的所有可能的正整数高
# 然后计算所有可能的宽，最后计算所有可能的周长，返回最小的周长。
def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    result = min(perimeters)
    return result

area = 80
# width(area, 5)

# perimeter(16, 5)

print("minimum_perimeter is: ", minimum_perimeter(area))

# [minimum_perimeter(n) for n in range(1, 10)]
