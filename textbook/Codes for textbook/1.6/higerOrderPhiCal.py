# implements a general method for iterative improvement and uses it to compute the golden ratio.

# 1.6 Higher-Order Functions: Iterative Improvement
#  improve函数是一个通用的迭代改进方法。它不指定正在解决什么问题：这些细节留给作为参数传入的update和close函数。
#  其中：guess是一个初始值，update是用来更新guess的函数，close是用来判断guess是否足够接近目标值的函数。
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

# the golden ratio的逼近计算公式
# 然后我们将他们写成一个golden_update函数，
# 这里的guess是一个初始值，可以是任意值。
def golden_update(guess):
    return 1/guess + 1

# 关于近似程度的计算，可以设定容忍误差。
# return True if its arguments are approximately equal to each other.
def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

## 对应close参数，传入的函数可以调整，计算不同要求的数值。这里我们希望计算the golden ratio
## 根据数学知识，我们希望 x*x 接近 x+1 可以得到the golden ratio。
def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

## 最后将四个函数组合起来使用，可以达到计算the gloden ratio的目的。
## improve（控制guess, close, update整体流程的函数）
## golden_update（决定如何update the guess number的函数）
## approx_eq（决定guess number和target number的差值，是否足够接近、满足误差要求的函数）
## square_close_to_suceessor（决定要guess 哪一类number的函数）
improve(golden_update, square_close_to_successor)

## For this test, no news is good news: improve_test returns None 
## after its assert statement is executed successfully.
from math import sqrt
phi = 1.6180339887498951   #the phi number
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'
    #assert approx_eq(12345, approx_phi), 'phi differs from its approximation'   #assert不通过会抛出assertionerror

improve_test()