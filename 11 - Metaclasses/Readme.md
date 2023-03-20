- how classes work
- type -> <class 'type'> is a metaclass, type defines rules to create any user defined class
- class Test:
    pass 
- Test = type('Test',(Foo,),{"x":5,"add_attribute":add_attribute})
- We can create own metaclass that inherits from type but change how object are created from the class created from our metaclass
- __new__ -> first thing called before object is initiated for the class. We can modify this dunder method to modify the way object is instantiated.
- __init__ -> Initializes object after it is created
- Metaclass can be powerful - It modifies construction for class if reqd. ex. change attribute name to upper case
- Enforce constraint on how classes created.