# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 我们要借助Python的@语法，把decorator置于函数的定义处
# 使用函数装饰器 A() 去装饰另一个函数 B()，其底层执行了如下 2 步操作：
# 将 B 作为参数传给 A() 函数；
# 将 A() 函数执行完成的返回值反馈回 B。
# 把@log放到now()函数的定义处，相当于执行了语句 now = log(now)
@log
def now():
    print('2015-3-25')

now()

def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log2('execute')
def now2():
    print('2015-3-25')

now2()