L = [x * x for x in range(10)]
print(L)

# 不比计算所有的项，节省空间
# 一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
for n in g:
    print(n)

# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)

# 我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
# 因为fib函数没有给出b的界限
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break