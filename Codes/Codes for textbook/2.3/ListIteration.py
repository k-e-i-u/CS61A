import pysnooper

# 使用while循环遍历list。
@pysnooper.snoop()
def count_while(s, value):
    """Count the number of occurrences of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == value:
            total = total + 1
        index = index + 1
    return total


# 使用for循环遍历list。
@pysnooper.snoop()
def count_for(s, value):
    """Count the number of occurrences of value in sequence s."""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

digits = [1, 8, 2, 8]


count_for(digits, 8)