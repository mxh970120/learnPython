import functools
# int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
int2 = functools.partial(int, base=2)
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
int2('1000000')
int2('1010101')
