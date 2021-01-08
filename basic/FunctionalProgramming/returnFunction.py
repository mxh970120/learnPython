# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)  # 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
print(f())  # 调用函数f时，才真正计算求和的结果


def count():
    fs = []
    for i in range(1, 4):
        def ff():
            return i*i
        fs.append(ff)
    return fs


# 返回的函数并没有立刻执行，而是直到调用了f()才执行
ff1, ff2, ff3 = count()  # 调用这三个函数时结果均为9，原因就在于返回的函数引用了变量i，但它并非立刻执行。
                         # 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
print(ff1())
print(ff2())
print(ff3())
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count2():
    def fff(j):
        def g():
            return j*j
        return g
    fss = []
    for i in range(1, 4):
        fss.append(fff(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fss

fff1, fff2, fff3 = count2()
print(fff1())
print(fff2())
print(fff3())