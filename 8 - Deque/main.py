import collections
from collections import deque

d = deque("hello")  # deque(iterable)
print(d)

#Methods for deque
#append 
d.append('4')
d.append(5)
print(d)
#append in beginning 
d.appendleft(5)
print(d)
#pop
d.pop()  # can provide index d.pop(index)
d.pop()
print(d)
#pop first element from beginning
d.popleft()
print(d)
#clear return empty deque
d.clear()
print(d)
#extend - adds iterable to end of list
d.extend('456') #d.extend(iterable) -> add iterable to end of list
d.extend('hello')
d.extend([1,2,3])
print(d)
#extendleft - adds iterable to start of list 
d.extendleft('hey')  # extend to left - so y first element
print(d)
#rotate
d.rotate(-2) #pos integer -> rotate to right, neg integer -> rotate to left
print(d)
# create deque with max length - remove elements at beginning if new elements added at end to keep length as maxlen
d=deque("hello",maxlen=5)
print(d)
d.append(1)
print(d)
d.extend([1,2,3])
print(d)
print(d.maxlen) #only access maxlen and not update it 