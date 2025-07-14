
## 1.1 名字name、值value、内存帧frame、环境environment
> 它们支撑了程序运行的基础：“名字name-值value”绑定在内存帧frame中，内存帧frame组成环境environment。

- 名字name：一个英文字符串，可以绑定值，**通过英文名字赋予值以意义、通过值让英文名字可以被编程计算，从而赋予编程以“抽象思想”**。
- 值value：参与计算机程序运行、表达式计算求值的基本对象。[[#2.1 基本表达式 primitive expressions|任意编程语言，都有多种类型的值，如 数字、字符串。]]
- 内存帧frame：解释器在内存中划分的一块空间，用于存储“名字-值”绑定、相同内存帧frame内部，名字不可重复。
- 环境environment：由一串内存帧frame组成，按照栈的FIFO规则，动态调整内存帧frame数量。
	- [[#1.2.2 函数定义声明 function definition statement|函数签名拥有创建local frame的所有必须信息]]
	- [[#1.1.4 求解mul(add(4, mul(4,6)), add(3,5))的例子| 一个正在运行的程序，永远有一个全局帧global frame，同时根据函数的调用动态创建local frame。]]

# 2 表达式
> 表达式expressions：描述某个计算过程。且所有表达式，都依赖环境environment进行“名字”查找和计算求值。

## 2.1 表达式的名字查找规则

- 所有“名字-值绑定”都保存在环境environment中。
- 所有表达式，都依赖环境environment进行“名字”查找和计算求值。
- “名字”查找时，按照从“local frame”到“global frame”的顺序，绑定最先匹配的“名字-值绑定”中的值，即使当前环境environment中的多个frame都有相同的“名字-值绑定”。

- 例子：
## 2.2 表达式的类型

- 按照书写格式，表达式有多种类型：
	- 基本表达式  primitive expressions
	- 算术表达式 arithmetic expressions
    - 函数调用表达式 function call expressions
### 2.2.1 基本表达式  primitive expressions
> 基本表达式：最原始的表达式，很直观、没有什么好解释的，如：3, 3.14, "hello"等。


```python
# 常见的基本表达式类型：
3 #整数
3.14  #浮点数
32.3e+18  #指数
9.322e-36j #复数
"Hello world" #字符串
True #布尔
["Hello", 1234, True]  #列表
("Hello", 1234, True)  #元组
{'Google', 'Facebook'}  #集合
```
### 2.2.2 算术表达式 arithmetic expressions
> 算术表达式：使用数学符号语言书写的单行代码。

- 例如：18+69, 6/23。
### 2.2.3 函数调用表达式 function call expressions
> 函数调用表达式：就是按“Operator(Operand, Operand, ...)”格式书写的代码。

![函数调用表达式的格式](image-5.png)

- 求解函数调用表达式，就是要递归求解Operators、Operands。
  - 递归求解Operators和Operands的值，顺序按照：先从左到右求解Operands，最后求解Operator。
  - 创建新local frame，绑定Operands值到函数签名中的formal parameters。
  - 执行函数体，将值向上递归返回，销毁当前local frame。
#### 2.2.3.1 求解mul(add(4, mul(4,6)), add(3,5))的例子
- 例子：求解 mul(add(4, mul(4,6)), add(3,5))
  - 求解add(4, mul(4,6))，由于也是function call expression，所以进入下一层递归，最后会得到28：
    - 求解4，得到4。
    - 求解mul(4, 6)，由于也是function call expression，所以进入下一层递归：
      - 求解4，得到4。
      - 求解6，得到6。
      - 求解mul，得到mul对应的函数：def mul(a, b)
      - 创建名为mul的local frame，绑定4, 6到a, b。
      - 执行mul的函数体，返回24，销毁名为mul的local frame。
    - 求解add，得到add对应的函数：def add(a, b)
    - 创建名为add的local frame，绑定4，24到a，b。
    - 执行add的函数体，返回28，销毁名为add的local frame。
  - 求解add(3,5)，由于也是function call expression，所以进入下一层递归，最后会得到8：
    - 求解3，得到3。
    - 求解5，得到5。
    - 求解add，得到add对应的函数：def add(a, b)。
    - 创建名为add的local frame，绑定3，5到a，b。
    - 执行add的函数体，返回8，销毁名为add的local frame。
  - 求解mul，得到mul对应的函数：def mul(a, b)
  - 创建名为mul的local frame，绑定28, 8到a, b。
  - 执行mul的函数体，返回224，销毁名为mul的local frame。
  - global frame得到mul(add(4, mul(4,6)), add(3,5))的返回值224。
  - 结束。
  
- 画出Expression Tree，理解函数调用表达式的递归求解过程。
![Expression Tree](image-1.png)
# 3 声明 statements
> 声明：描述了某个动作，且最终将通过解释器执行动作。A statement is executed by the interpreter to perform an action

- 声明有多种类型：
  - 引用声明 import statements
  - 赋值声明 assignment statements
  - 函数定义声明 function definition statements
  - 混合声明 compound statements
## 3.1 引用声明 import statements
```python
# python 引用声明的例子
from operator import mul
import pandas as pd
```

## 3.2 赋值声明 assignment statements
> 赋值声明：按“left = right”格式书写的代码，最终将right的值，和left的名字绑定，**是“抽象”技术，将值，抽象成变量名**。

- 赋值生命的执行规则：
![赋值声明执行动作](image-2.png)

- 例子： a, b = 2, 3 + 3
  - 等号左边求值：2 求值得到 2， 3 + 3 求值得到6。
  - 绑定到等号右边：a绑定2，b绑定6。
## 3.3 函数定义声明 function definition statements

> 函数定义声明：一个函数包括“函数签名”和“函数体”， **是“抽象”技术，将计算过程，抽象成函数签名**。

- 函数定义声明的书写格式：
![函数定义声明|900](image-3.png)

- 函数定义声明的执行动作：创建函数签名、设置函数体、绑定函数签名和函数体。
![函数定义声明的执行动作|900](image-4.png)

- 用户自定义函数的生命周期：
![[Pasted image 20240430111937.png]]



## 3.4 混合声明 compound statements
> 混合声明：是一个复杂的代码块，由一个或多个header，和1:1对应的statements suite组成，解释器根据header的结果、选择性执行对应statements suite。

- 混合声明的结构：
![[Pasted image 20240430113344.png]]

- 常见的混合声明：
	- if-elif-else 声明。
	- while 声明。
	- for 声明。
	- switch-case 声明。
	- 函数定义声明。

