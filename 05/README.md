# 第 5 章 一等函数

## 5.1 把函数视作对象

```python
factorial.__doc__
help(factorial)
```

* map 函数返回一个可迭代对 象，里面的元素是把第一个参数（一个函数）应用到第二个参数（一个可迭代对象，这里 是 range(11) ）中各个元素上得到的结果

## 5.2 高阶函数

* 接受函数为参数， 或者把函数作为结果返回的函数是高阶函数
* 可选的  key 参数用于提供一个函数， 任何单参数函数都能作为 key 参数的值

**现代替代品**

* 列表推导或生成器表达式具有 map 和 filter 两个函数的功能，而且 更易于阅读

```python
from functools import reduce
from operator import add

reduce(add, range(100))

sum(range(100))
```

**归约**

* all(iterable): 如果 iterable 的每个元素都是真值
* any(iterable): 只要 iterable 中有元素是真值


## 5.3 匿名函数

* lambda 关键字在 Python 表达式内创建匿名函数。
* 在参数列表中最适合使用匿名函数
* 除了作为参数传给高阶函数之外， Python 很少使用匿名函数

```python
sorted(fruits, key=lambda word: word[::-1])
```

## 5.4 可调用对象

* 如果想判断对象能 否调用，可以使用内置的 callable() 函数

## 5.6 函数内省

* `dir()`

## 5.7 从定位参数到仅限关键字参数

## 5.8 获取关于参数的信息

* `__defaults__`、`__code__`

```python
from inspect import signature

```

## 5.9 函数注解

**5.10.2 使用 functools.partial 冻结参数**

* 部分应用是指，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定