import inspect 

x = [1,2,3]
y = [4,5]

#syntax using below on list object is implemented under the hood using dundar methods
print(type(x))
print(x) #print list with space even though not defined in x. 
print(x+y)
print(len(x))
print(x[1]) #indexing

#x and y are objects - we can perform operations using python syntax. This operation implemented on list object and tells list object on 
#how to behave 

class Person:
    def __init__(self,name):  #dunder method 
        self.name=name 
        
    def __repr__(self): #define string representation of object from inside
        return f"Person({self.name})"
    
    def __mul__(self,x):#define when multiplication operation on person objects , maske sure these operations are type safe based on exception below 
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")
        self.name=self.name*x
        
    def __call__(self,y):
        print(y)
        
    def __len__(self):
        return len(self.name)
        
p = Person("Tim")
print(p)  #it prints memory address as we have not told how to print object of class person if no repr method available else use the repr method
p*3  #using __mul__ method here
print(p)
p(4) #using __call__ method here ; () -> __call__ method
print(len(p))


#############################################################################
print("\n\n")
from queue import Queue
import inspect 

q=Queue()
print(q)  # this class doesnt implement __repr__ method

print(inspect.getsource(Queue))

# Create your own Queue class similar to what we have and implement repr or + operation 
from queue import Queue as q 

class Queue(q):  #Here create your own class that inherits from parent class queue and implement your own dunder methods here
    def __repr__(self):
        return f"Queue({self._qsize()})"
    
    def __add__(self,item):
        self.put(item)
        
    def __sub__(self,item):
        self.get()

qu=Queue() #uses the defined repr dunder method above 
qu+9 
qu+7
qu-0
print(qu)
    
    
    
    
    


