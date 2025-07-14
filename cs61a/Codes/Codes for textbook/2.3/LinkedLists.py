import pysnooper

## 下面的代码是用PYTHON LIST来实现PYTHON LINKED LIST
empty = 'empty'

# LINKED LISTS的判断函数
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

# 单节点LINKED LISTS的构造函数
# 需要手动构造多节点的Linked list，如：link(3,link(2,link(1,empty)))
def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

# 迭代版本 n,m partition的专用LINKED LIST构造器
def linked_partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty) # A list containing the empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = linked_partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = linked_partitions(n, m-1)
        return extend_link(with_m, without_m)

# 辅助可视化打印linked_partition结果的函数
def print_partitions(n, m):
    lists = linked_partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))

# LINKED LISTS的选择器
def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

# LINKED LISTS的选择器
def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

# LINKED LISTS的长度查询器
# 迭代版本
def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

# LINKED LISTS的元素选择器
# 迭代版本
def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

# LINKED LISTS的长度查询器
# 递归版本
def len_link_recursive(s):
    """Return the length of a linked list s."""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))

# LINKED LISTS的元素选择器
# 递归版本。
# LINKED LIST是一种递归结构的DATA ABSTRACTION
def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)

# 链尾新增插入节点的函数
# 递归实现
def extend_link(s, t):
    """Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

## 迭代实现apply a function on all elements
def apply_to_all_link(f, s):
    """Apply f to each element of s."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

## 递归实现LINKED LIST的过滤器filter based on function f.
def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept
        
## 递归实现LINKED LISTED拼接成字符串
def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)



## 测试用例
four = link(1, link(2, link(3, link(4, empty))))
one = link(5, empty)

# first函数返回当前链表节点的第一个元素，也就是当前节点存储的值
# first(four)

# # rest函数返回当前链表节点的第二个元素，也就是当前节点的下一个节点索引
# rest(four)

# # 通过不断嵌套调用rest函数，可以按照链接顺序获取到链表的每个元素
# first(rest(four))
# first(rest(rest(four)))

# # 查询当前链表的长度
# len_link(four)
# len_link_recursive(four)

# # getitem_link函数返回当前链表节点的第i个元素
# getitem_link(four, 0)
# getitem_link_recursive(four,0)

# 测试用例
# extend_link(four, one)

# 测试用例
# apply_to_all_link(lambda x: x * x, four)

# 测试用例
# keep_if_link(lambda x: x%2 == 0, four)

# 测试用例
# join_link(four, ", ")

# 测试用例
linked_partitions(6,4)