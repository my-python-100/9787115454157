# 第7章 函数装饰器和闭包


## 7.1 装饰器基础知识

## 7.2 Python何时执行装饰器

* 它们在被装饰的函数定义之后立即运行

## 7.4 变量作用域规则

* Python 不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量
* 想让解释器把b当成全局变量，要使用 global 声明

## 7.5 闭包

* 闭包， 它能访问定义体之外定义的非全局变量
* 自由变量: 未在本地作用域中绑定的变量

```python
__code__.co_varnames
__code__.co_freevars
__closure__

# cell_contents
```

## 7.6 nonlocal 声明

* 它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了

## 7.7 实现一个简单的装饰器
