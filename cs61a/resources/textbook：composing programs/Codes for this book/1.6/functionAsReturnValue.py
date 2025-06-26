## We can achieve even more expressive power in our programs by creating functions whose returned values are themselves functions.

def square(x):
    return x * x

def successor(x):
    return x + 1

# 在python编码规范中
# 可以用compose1，加一个自然数1，来提示我和其他使用者
# 这里作为参数传入的函数，应当只接受一个参数的规约，
# 以此来规避高阶函数带来的漏洞。
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h   # nested functions maintain their enclosing environment when they are returned. 

## never called
## because h(x) follow the lexical scoping rule.
def f(x):
    """Never called."""
    return -x

## h(x) will get parameter f firstly, in which, f is corresponding to function "square"
square_successor = compose1(square, successor)
result = square_successor(12)
print(result)