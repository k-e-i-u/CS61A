import pysnooper

# Another common pattern of computation is called tree recursion, 
# in which a function calls itself more than once. 

# As an example, consider computing the sequence of Fibonacci numbers,
# in which each number is the sum of the preceding two.

# 其实树递归（TREE RECURSION）解斐波那契数列的效率不高。
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

result = fib(6)

# 但是树递归也有它的优点。
# 例如，我们使用树递归计算一个正整数的分割。

# 正整数 n 的分割数是指用 m 以内的正整数各部分之和按递增顺序表示 n 的方法的个数。
# 例如，用 4 以内的部分对 6 进行分割的方式一共是9种。

# 定义一个函数 count_partitions(n,m)，它返回使用最大为 m 的整数对 n 进行不同分割的次数：
# 我们使用递归的方法设计这个函数。那么，首先思考，如何缩小问题，Base Case 是什么，以及recursion jump of faith。
# 使用不超过 m 的整数分割 n 的方法数等于：
# （1）使用最大为 m 的整数对 n-m 进行分割的方式数，
# （2）使用最大为 m-1 的整数对 n 进行分割的方式数。
# Base Case是分割 0 ：
# （3）There is one way to partition 0: include no parts.
# （4）There are 0 ways to partition a negative n.
# （5）There are 0 ways to partition any n greater than 0 using parts of size 0 or less.

@pysnooper.snoop()
def count_partitions(n, m):
    #base case：当要分割的数n为0时，说明当前分割的方式有效，返回1。
    if n == 0:
        return 1
    #base case：当要分割的数n小于0时，说明当前分割的方式无效，返回0。
    elif n < 0:
        return 0
    #base case：当要分割的数n大于0，且分割的最大数m为0时，说明当前分割的方式无效，返回0。
    elif m == 0:
        return 0
    # 设计树递归求解正整数分割次数问题。递归设计核心目标是要将问题分解成更小的子问题。
    # 在当前递归阶段，count_partitions(n, m) 时，缩小问题规模的方式是：
    # （1）使用当前m对n进行分割，并得到分割方式的个数。
    # （2）使用m-1对n进行分割，并得到分割方式的个数。
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
    

def main():
    """Main function to test all debugging methods."""
    try:
        count_partitions(6, 4)

    except AssertionError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

