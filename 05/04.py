# 5.10 支持函数式编程的包
from functools import reduce
from operator import add

def fact(n):
  return reduce(mul, range(1, n+1))


# 能替代从序列中取出元素或读取对象属性的lambda表达式

# itemgetter(1)
# lambda fields: fields[1]

## 如果把多个参数传递给itemgetter, 它构建的函数会返回提取值构成的元祖


# attrgetter('name', 'coord.lat')

# methodcaller, 创建的函数会在对象上调用参数指定的方法
