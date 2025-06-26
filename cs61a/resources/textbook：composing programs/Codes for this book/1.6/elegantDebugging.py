from typing import Any
import pysnooper
from icecream import ic

def some_function() -> int:
    """Simple function with breakpoint debugging."""
    x = 42
    breakpoint()  # python version >= 3.7
    y = x + 1
    return y

def divide(a: float, b: float) -> float:
    """
    Divide two numbers with assertion check.
    
    Args:
        a: dividend
        b: divisor
    Raises:
        AssertionError: if b is zero
    """
    assert b != 0, "除数不能为 0"
    return a / b

# pysnooper是一个装饰器，可以为函数添加运行日志监控，并且输出到log文件。
@pysnooper.snoop(output='./debug.log')  
def calculate_snooper() -> int:
    """Function with snooper debugging."""
    x = 42
    y = x + 1
    return y

# pysnooper的装饰器不加参数时，会将调试日志推送到标准输出流，也就是控制台。
@pysnooper.snoop()  
def calculate_snooper_no_out() -> int:
    """Function with snooper debugging."""
    x = 42
    y = x + 1
    return y

# icream是一个调试工具，可以在代码中插入调试信息，并且输出到控制台。
def calculate_icecream() -> int:
    """Function with icecream debugging."""
    x = 42
    ic(x)  # 输出：ic| x: 42
    result = x * 2
    ic(result)  # Add result tracking
    return result

def main():
    """Main function to test all debugging methods."""
    try:
        # Test divide function
        print(divide(10, 2))
        # print(divide(10, 0))  # This will raise AssertionError
        
        # Test icecream debugging
        # result = calculate_icecream()
        # ic(result)
        
        # Test snooper debugging
        result_snooper = calculate_snooper_no_out()
        print(f"Snooper result: {result_snooper}")
        
    except AssertionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()