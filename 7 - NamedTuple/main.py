import collections
from collections import namedtuple

Point = namedtuple('Point','x y z')  # namedtuple(<name>,<fields> as iterable object), this will breakdown fields for object for Point in x, y and z
#alternate way Point = namedtuple('Point',['x', 'y', 'z'])
#Point = namedtuple('Point',{'x':0, 'y':0, 'z':0})
#treat Point as a class and create objects of it 
newP = Point(3,4,5)
print(newP)

#Methods for named tuple
print(newP.x, newP.y, newP.z)  #access named tuple by field name
print(newP[0], newP[1], newP[2])  #access named tuple by index
print(newP._asdict())  #access named tuple in form of dict
print(newP._fields)  #access all field names

newP = newP._replace(y=6) #update field value for an object to a new object as tuple are immutable
print(newP)

p2= Point._make(['a','b','c'])  #assign list to field names and create a new namedtuple
print(p2)