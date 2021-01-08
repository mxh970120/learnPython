# you need unpack N elements from an iterable, but the iterable may be longer than N elements,
# causing a "too many values to unpack" exception.

# example 1
def drop_first_last(grades):
    first, *middle, last = grades
    return middle


A = [1, 2, 3, 4]
print(drop_first_last(A))

# example 2
records = [('foo', 1, 2), ('bar', 'hello',), ('foo', 3, 4)]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

    
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)