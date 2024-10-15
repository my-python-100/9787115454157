# 第 1 章 Python数据类型

|本期版本|上期版本 
|:---:|:---:
`Tue Oct 15 12:03:26 CST 2024` | -

## 1.1 一摞Python风格的纸牌

* [使用collections中的namedtuple來操作簡單的物件結構 | Drake's](https://qiubite31.github.io/2017/03/02/%E4%BD%BF%E7%94%A8collections%E4%B8%AD%E7%9A%84namedtuple%E4%BE%86%E6%93%8D%E4%BD%9C%E7%B0%A1%E5%96%AE%E7%9A%84%E7%89%A9%E4%BB%B6%E7%B5%90%E6%A7%8B/)
* <https://docs.python.org/3/library/collections.html>
* <https://baike.baidu.com/item/%E8%8A%B1%E8%89%B2/15500441>
* <https://docs.python.org/3/library/random.html>

## 1.2 如何使用特殊方法

* 特殊方法的存在是为了被 Python 解释器调用的， 你自己并不需要调用它们
* [octest 用法简介 | Yunfeng's Simple Blog](https://vra.github.io/2021/02/02/doctest-intro/)

**1.2.2 字符串表示形式**

* 有一个内置的函数叫 repr ，它能把一个对象用字符串的形式表达出来以便辨认，这 就是“字符串表示形式”
* repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字符串 表示形式的
* 和 __str__ 的区别在于， 后者是在 str() 函数被使用， 或是在用 一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。print函数

**1.2.4 　自定义的布尔值**

* bool(x) 的背后是调用 x.__bool__() 的结果
* 如果不存在 __ bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()

## Ref


* <https://docs.python.org/3/reference/datamodel.html>
* [Python 中 __name__ 有什么用](https://www.freecodecamp.org/chinese/news/python-name/)
