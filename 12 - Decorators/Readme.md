- Modify behaviour of function without modifying the code of that function
- useful while debugging a function
- decorator add one line of code and change behaviour of function using @ at the top of the function whose behaviour needs to be modified without changing the code 
- decorator returns the wrapper method as an object (memory address)
- func3 = func(func3) 
- alternate way of calling using decorator below
        @func 
        def func3():
            pass
- To use decorators with any functions with any number of arguments use *args and **kwargs
        def func(f):
            def wrapper(*args, **kwargs):
                print("Started")
                f(*args,**kwargs)
                print("Ended")
        return wrapper
- To use decorators with any functions with any number of arguments that also return a value 
        def func(f):
            def wrapper(*args, **kwargs):
                print("Started")
                rv=f(*args,**kwargs)  #store return value so you can access it later when new function is called
                print("Ended")
            return rv 
        return wrapper
- Example of decorator functions 
    - decorator to calculate the time it takes for any function to execute 
    - decoartor to log whats happening in any function
    - decorator to validate input for any functions