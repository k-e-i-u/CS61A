## ！！！本代码实现的tree都是玩具级别的
## 后续请学习python的github 数据结构实现。
## 以及algorithms等书的实现。

import pysnooper
# 使用python list嵌套组合的方式，实现简单版本的TREE DATA ABSTRACTION

# 树的构造器
# 一棵树只有在有根标签且所有分支都是树的情况下才是形式良好的树。
# 在树的构造函数中使用is_tree函数来验证所有分支是否都是形式良好的树。
def tree(root_label, branches=[]):
    # assert is_tree(root_label)
    for branch in branches:
        assert is_tree(branch)
    return [root_label] + list(branches)

# 返回当前节点的label值
def label(tree):
    return tree[0]

# 返回当前节点的子树列表
def branches(tree):
    return tree[1:]

# 接下来根据tree的定义，通过递归的方式，实现is_tree函数。
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# 判断当前节点是否是叶子节点
# 叶子节点的定义是没有分支的树
# 也就是branches函数返回的列表长度为0
# python中len([]) == 0
def is_leaf(tree):
    return not branches(tree)

# 测试一下当前数据结构
# t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
# print(t)  # [3, [1], [2, [1], [1]]]
# print(label(t))  # 3
# print(branches(t))  # [[1], [2, [1], [1]]]
# print(label(branches(t)[1]))  # 2
# print(is_leaf(t))  # False
# print(is_leaf(branches(t)[0]))

# Add these test bad-cases

# case 1: root的label是空的
# t = tree([], [tree(1), tree(2, [tree(1), tree(1)])])

# # case2：子节点底层数据结构不是list，而是int。
# # 事实上，这个错误是因为data abstraction的实现不够严谨，导致了错误的树结构。
# t = tree([3], 2)

# # case3：子节点底层数据结构是空的双层list。
# t = tree([3], [[]])


## 定义fib-tree 斐波那契树
## 斐波那契数列为：0，1，1，2，3，5，8，13，21，34，55，89…
# @pysnooper.snoop()
def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

# print(fib_tree(5)) 

# 使用迭代的方式，实现计算树的叶子节点数量
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)



#        5
#     /      \
#    2        3
#  /   \    /   \
# 1    1   1     2
#    / \  / \   / \
#   0   1 0  1  1  1
#                 / \
#                0   1
# print(count_leaves(fib_tree(5)))  # 8

# print(count_leaves(tree(3, [tree(1), tree(2, [tree(1), tree(1)])])))


## partition tree，用于进行number partition的树结构
#  并且将partition的结果存储在tree中。
#  Partition trees. 
# Trees can also be used to represent the partitions of an integer. 
# A partition tree for n using parts up to size m is a binary (two branch) tree 
# that represents the choices taken during computation. 
# In a non-leaf partition tree:
# the left (index 0) branch contains all ways of partitioning n using at least one m
# the right (index 1) branch contains partitions using parts up to m-1, and
# the root label is m.
# The labels at the leaves of a partition tree express whether the path from 
# the root of the tree to the leaf represents a successful partition of n.

# @pysnooper.snoop()
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

print_parts(partition_tree(6, 4))

# 这是之前simple tree recursion实现number partition的代码。
# 这个只能count partition的次数，而不能返回partition的具体结果。
# @pysnooper.snoop()
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

print(count_partitions(6, 4))

