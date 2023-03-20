
def func(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")
        
    return wrapper()

x=func("hello")

print("")

def func(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")
        
    return wrapper

x=func("hello")
print(x) #store function memory address in x 
x() #calling the function from the memory address, functions in python are objects - pass them around as arguments. 


#pass function to another function 
print("\n\n")
#function func is a decorator that changes the behaviour of the passed function parameter f
def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
        
    return wrapper

def func2():
    print("I am func2")
    
def func3():
    print("I am func3")
    
x=func(func2)  #Change behaviour of multiple functions examples below - func2 and func3 here 
print(x)
print(x())

y=func(func3)
print(y)
print(y())


# Alternate way of calling func3 with func decorator
print("\n\n")
print("func3")
func3()
func3 = func(func3) #func3 variable here - store function return from call of func so change behaviour of func3 after passed through func
print("Decorated func3")
func3()


#To replace the line func3 = func(func3), use @func 
print("\n\n")
@func  #decorate syntax
def func2():
    print("I am func2")
    
func2()
#we can decorate function with multiple functions 

#Stepf for decorator 
#1. create a function that includes wrapper functionality and return wrapper 
#2. create the new function that uses the decorator using @symbol before new function definition

#function with parameter that needs to be decorated 


print("\n\n")

def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        f(*args,**kwargs)
        print("Ended")
        
    return wrapper

@func  
def func2(x): #wrapper function needs same number of arguments as wrapper function, so use unpacked agruments in wrapper method
    print(x)
    
@func  
def func3():
    print("This is func3")
    
func2(5)
func3()


#function return value 
print("\n\n")

def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        rv=f(*args,**kwargs)  #store return value so you can access it later when new function is called
        print("Ended")
        return rv
        
    return wrapper

@func  
def func2(x,y): #wrapper function needs same number of arguments as wrapper function, so use unpacked agruments in wrapper method
    print(x)
    return y 

x = func2(5,6)
print(x)

#Example useful decorator examples 

#Validate user input using decorator for any function or time diff functions
#not touch main function when adding extra functionality, just need to add top of function using @

import time 

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        rv=func()
        total=time.time()-start
        print("Time",total)
        return rv 
    return wrapper 

@timer
def test():
    for _ in range(100000):
        pass 
    
@timer 
def test2():
    time.sleep(2)
    
test()
test2()

#decorator modify behaviour of function without actually modifying the function
#another is logging decorator for whats happening in function
#validating input for a function
