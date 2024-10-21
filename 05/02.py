# 5.8 获取关于参数的信息

from inspect import signature

def clip(text, max_len=80):
  '''在max_len前后'''
  pass

# 参数默认值，要从后向前扫描
print(clip.__defaults__)
print(clip.__code__)
# 参数名字,还有局部变量
# 不包含前缀为*或者**的变长参数
print(clip.__code__.co_varnames)
# 参数名称是前N个字符串，N的可以通过下面获取
print(clip.__code__.co_argcount)

# inspect
sig = signature(clip)
print(sig)