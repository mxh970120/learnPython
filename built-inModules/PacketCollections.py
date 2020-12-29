from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2']) # key2不存在，返回默认值

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# chainmap

# Counter是一个简单的计数器，例如，统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
c.update('hello')  # 也可以一次性update
print(c)
