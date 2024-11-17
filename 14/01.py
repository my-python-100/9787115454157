s = "ABC"

# 使用可迭代的对象构建迭代器
it = iter(s)
print(next(it))
print(next(it))

# StopIteration异常表明迭代器到头了