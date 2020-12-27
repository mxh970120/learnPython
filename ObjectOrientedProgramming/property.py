class Student(object):

    def get_score(self):
         return self._score

    # 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)  # ok!
s.get_score()

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 解决方法：使用property
class Student2(object):
    # @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
    # 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s2 = Student()
s2.score = 60 # OK，实际转化为s.set_score(60)
s2.score # OK，实际转化为s.get_score()


class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def age(self):
        return 2015 - self._birth

