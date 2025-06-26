import pysnooper

# python list有一个unpacking的特性，可以将一个嵌套列表里的任意子列表，同时赋值给多个变量。
pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]

same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1

print('相同的数量是：', same_count)