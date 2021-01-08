# you want to keep a limited history of the last few items seen during iteration or
# during some other kind of processing

from collections import deque

# using deque(maxlen = N) creates a fixed-sized queue
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

# example 2
q2 = deque()
q2.append(1)
q2.append(2)
q2.append(3)
print(q2)
q.appendleft(4)
print(q2)
print(q2.pop())
print(q2)
print(q2.popleft())
print(q2)
