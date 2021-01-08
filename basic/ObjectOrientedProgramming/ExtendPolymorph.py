class Animal(object):
    def run(self):
        print('Animal is running...')


# 继承
class Dog(Animal):

    # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
    # 多态
    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
def run_twice(animal):
    animal.run()
    animal.run()


class Mammal(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


# 多重继承
class Dog2(Mammal, Runnable):
    pass

# 如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Dog2除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class Dog3(Mammal, RunnableMixIn):
    pass