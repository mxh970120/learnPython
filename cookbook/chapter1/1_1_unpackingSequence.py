# you have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

# example 1
p = (4, 5)
x, y = p
print(x, y)

# example 2
data = ["name", 1, (2, 3)]
a, b, c = data
print(a, b, c)
a, b, (c, d) = data
print(a, b, c, d)

# example 3
s = "Hello"
a, b, c, d, e = s
print(a, b, c, d, e)

# example 4
s = "Byebye"
# _, b, c, d, _ = s  # error! must the same amount
_, b, c, d, _, f = s
print(b, c, d)
