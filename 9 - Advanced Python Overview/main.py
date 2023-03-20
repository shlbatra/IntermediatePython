'''
Python code run and executed ?
Interpreted programming language 

Compiler - compile high level code to lower level byte code. 
Interpreter - takes some code (byte), interpret to machine code and execute code.ex. C -> compile directly to machine code and run so not need interpretor with C

Python execution chain ->
High Level Code -> transalate to Byte code (check syntax) -> Interpretor read byte code and translate to machine code in live time 
and execute on machine
Need Interpretor so hard to run code on mobile devices. 

'''

class Dog:
    def __init__(self):
        self.bark()  #code not work in other languages as method not defined but works in python as code is executed in run time and not compile time. 
        #Compile just translate but not check for code validation so could be an issue if not picked before deploying to Prod. 
        
####################################################################################

def make_class(x):  #define class in function as code validation is not checked
    class Dog:
        def __init__(self, name):
            self.name=name 
            
        def print_value(self):
            print(x)
            
    return Dog #return class itself but not object 
    
cls = make_class(10)  #return class - cls, Function here is a class constructor
print(cls)  #code executing on fly so all things defined store in memory so dog class has memory, same with function and variables. We can interact with them live
#O/P -> <class '__main__.make_class.<locals>.Dog'>
#main is the main module, make class -> name of function defined, locals defines what is inside function , Dog is the class
    
d = cls("Tim") #use class to create its object
print(d.name)
d.print_value()    


####################################################################################
print("\n\n")
for i in range(10):  #function defined inside loop, one show only exist and will be overwritten 10 times 
    def show():
        print(i*2)
        
    show()
print("\n\n") 
for i in range(10):  #Last show defined will be used at the end
    def show():
        print(i*2)
        
show()
    
####################################################################################
print("\n\n")
def func(x):   # A function returns another function
    if x == 1:
        def rv():
            print("X is equal to 1")
    else:
        def rv():
            print("X is not equal to 1")
    return rv 

new_func = func(1)
print(new_func)
new_func()        

####################################################################################
print("\n\n")

#Everything in Python is an object that is run in real time so each of the object has a memory address that can be passed around Python program
#How Inspect functions in Python ?

import inspect #inspect objects in real time 
from queue import Queue  

print(id(new_func))   #get memory address of our function/object passed

print(inspect.getmembers(new_func))  #Get metadata info about function
print("\nSource Code")
print(inspect.getsource(new_func)) #get source code about function
print("\nSource Code - Queue")
print(inspect.getsource(Queue))
    
    
    
    
    
    
        
        
        
