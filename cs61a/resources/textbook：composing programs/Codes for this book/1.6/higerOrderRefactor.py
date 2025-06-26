# 三个函数，具有common pattern，可考虑重构出higher order function
# 构造了高阶函数“summation”，
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
    return total


# summation是一个高阶函数。
# 该函数通过进一步抽象，表达了更高层级、更通用的summation的概念，
# 而不是局限在sum naturals, sum cubes等特定的sum计算概念。
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

# 计算sum_naturals时，直接传入一个term函数，用于指定数据生成规则
def identity(x):
        return x

def sum_naturals2(n):
    return summation(n, identity)

# 根据传入term函数的不同，可以计算不同的summatino任务
# 这里传入pi_term，就可以计算pi_sum。
def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

def pi_sum2(n):
    return summation(n, pi_term)

# HIGHER-ORDER FUNCTION的劣势：
# 作为参数传入的函数，其签名所接受参数的个数
# 必须满足高阶函数体内算法的要求，否则就会报错
# 比如 def cube_term(x, y)就不适用于summation(n, term)函数
def cube_term(x):
    return x * x * x


import timeit

# 通过 globals() 传递当前全局变量
duration = timeit.timeit(
    stmt='sum_naturals(9999)',  # 直接调用函数（不打印，避免耗时干扰）
    globals=globals(),          # 关键：继承当前作用域
    number=10000
)
print(f"sum_naturals 平均耗时：{duration / 10000} 秒")


# 通过 globals() 传递当前全局变量
duration = timeit.timeit(
    stmt='sum_naturals2(9999)',  # 直接调用函数（不打印，避免耗时干扰）
    globals=globals(),          # 关键：继承当前作用域
    number=10000
)
print(f"sum_naturals2 平均耗时：{duration / 10000} 秒")
