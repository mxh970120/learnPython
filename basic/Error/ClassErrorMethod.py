class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        # 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
        # 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo('0')

def bar():
    try:
        foo('0')
    except ValueError as e:
        # 打印一个ValueError!后，又把错误通过raise语句抛出去了
        # 捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
        print('ValueError!')
        # raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
        raise

bar()