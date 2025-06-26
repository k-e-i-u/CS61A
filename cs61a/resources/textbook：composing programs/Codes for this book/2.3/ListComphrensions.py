# python中，list具备一种list comphrension的技术
# 可以通过一个表达式，来创建一个新的list


odds = [1, 3, 5, 7, 9]
print([x+1 for x in odds])
print([x for x in odds if 25 % x == 0])