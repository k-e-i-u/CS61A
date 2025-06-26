## we can create function values on the fly using lambda expressions, 
# which evaluate to unnamed functions. A lambda expression evaluates 
# to a function that has a single return expression as its body. 
# Assignment and control statements are not allowed.

def compose1(f, g):
    return lambda x: f(g(x))

# 将lambda expression用作函数生成器，生成一个函数，并作为参数传入compose1函数。
f = compose1(lambda x: x * x,
             lambda y: y + 1)

result = f(12)