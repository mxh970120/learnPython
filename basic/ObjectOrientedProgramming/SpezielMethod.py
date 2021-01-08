class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))


class Student2(object):
    def __init__(self, name):
        self.name = name
        self.age = 18

    # 改写了str类，使得输出变化
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # 直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
    __repr__ = __str__

    # 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
    # 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
    def __iter__(self):
        return self

    def __next__(self):
        self.age = self.age + 1  # 计算下一个值
        if self.age > 50:  # 退出循环的条件
            raise StopIteration()
        return self.age  # 返回下一个值

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    # list还有切片的功能，也需要单独实现，具体可以查询list的源码
    def __getitem__(self, n):
        return self.age + n + 1

    # 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。此处为number
    # 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
    # 作用就是，可以针对完全动态的情况作调用。比如URL，不需要对每一个URL做个属性
    def __getattr__(self, attr):
        if attr == 'number':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
    def __call__(self):
        print('My name is %s.' % self.name)


print(Student2('Michael'))

for n in Student2('Michael'):
    print(n)

print(Student2('Michael')[5])

print(Student2('Michael').number)

s = Student2('Michael')
s()
