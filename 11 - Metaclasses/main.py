'''
how class created, instantiated and worked on
what metaclasses are, how they work and when to use them 
'''

'''
we can do this here because classes are objects, interact in run time, pass it around as parameters, class creates objects as well
class is object itself - higher level class that created class. Class defines rules for object - methods,attributes, parameters, operations 
metaclass defines rules for class
'''

def hello():
    class Hi:
        pass    
    return Hi 

'''

Output of class -> <class '__main__.Test'>, get this because class itself is an object

Output of object -> <__main__.Test object at 0x10113dfa0>
in main method, object of class test at a jibberish memory location
'''

class Test:
    pass 

print(Test)
print(Test())

def func():
    pass

print(type(Test)) #<class 'type'> -> metaclasses, type defines rules and create test class for us
print(type(2)) # <class 'int'>
print(type(func)) # <class 'function'>
print(type(Test())) #<class '__main__.Test'>



print("\n\n")  


class Foo:
    def show(self):
        print("hi")

def add_attribute(self):
    self.z=9

#we can create class from type class as well directly 
Test = type('Test',(Foo,),{"x":5,"add_attribute":add_attribute})  #equivalent to Test class created using class keyword, type function creates class with (name,basis - parentclass inherit from, attributes )
print(Test)
print(Test())
t=Test()
t.wy="hello"
print(t.x)
print(t.wy)
t.show()
t.add_attribute()
print(t.z)

print("\n\n\n")
#metaclasses - class abive the class we create , pass to metaclass and return object that represents a class

#create own metaclass inherit from type but change how object are created 
#type parameters -> type(name,bases,attrs)

class Meta(type):
    def __new__(self,class_name,bases,attrs): #before the init method - first thing called before object instantiated, modify the way object is instantiated, init - initializes object after it is created
        print(attrs)
        
        a={}
        for name,val in attrs.items(): #change attribute name to upper case for any class defined using metaclass
            if name.startswith("__"):
                a[name]=val
            else:
                a[name.upper()]=val
        print(a)
        return type(class_name,bases,a)

class Dog(metaclass=Meta): #change to our own metaclass, print attrs and return class
    x=5
    y=8
    def hello(self):
        print("hi")
    
'''
Output - {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 8}
attribute printed above, module -> name, qualname (class name), then attributes defined for class x, y and hello.
'''

#metaclass can be powerful - modify construction for class if reqd. ex. change attribute name to upper case
d = Dog()
print(d.X) #upper case attribute now based on metaclass        
    
# Enforce constraint on how classes created. ex. Class defined to have specific attribute. use in library code. 
#metaclass can inherit from other metaclasses.




