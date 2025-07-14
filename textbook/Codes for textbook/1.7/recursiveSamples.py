import pysnooper

# Example: sum natural numbers in recursive way
# Break down the big problem: to sum the digits of a number n, add its last digit n % 10 to the sum of the digits of n // 10.
# The Special cases:  if a number has only one digit, then the sum of its digits is itself.

# pysnooper的装饰器不加参数时，会将调试日志推送到标准输出流，也就是控制台。
@pysnooper.snoop()  
def sum_digits(n):
    # special case. And the base case/exit of recursion.
    # a conditional statement that defines the behavior of 
    # the function for the inputs that are simplest to process. 
    if n < 10:
        return n
    # The base cases are then followed by one or more recursive calls. 
    # Recursive calls always have a certain character: they simplify the original problem.
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last


# 计算n!的函数，迭代版本。
# The iter version must introduce two additional names, 
# total and k, that are not required in the recursive implementation.
@pysnooper.snoop()
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

# 计算n!的函数，递归版本。
@pysnooper.snoop()
def fact_recur(n):
    if n == 1:
        return 1
    else:
	    return n * fact_recur(n-1)


def main():
    """Main function to test all debugging methods."""
    try:
        # result_sum_digits = sum_digits(12345)

        # result_fact_iter = fact_iter(5)

        # result_fact_recur = fact_recur(5)

        # result = is_even(4)

        play_bob(3)  # 测了很多遍，感觉Bob总是赢。
    
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

