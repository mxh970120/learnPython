d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

# 实现类似其他语言的迭代
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iterable 和 Iterator
from collections import Iterable
print(isinstance('abc', Iterable))  # str是否可迭代
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代
print(isinstance(123, Iterable))  # 整数是否可迭代


from collections import Iterator
# list、dict、str虽然是Iterable，却不是Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))


