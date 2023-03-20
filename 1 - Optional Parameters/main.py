def func(x):    # x is a parameter here 
    return x**2

call=func(5)
print(call)

#optional parameter

def func(x=2):    # x is a optional parameter here with default value 
    return x**2

call=func()
print(call)

#multiple optional and non optional parameter

def func(word,freq):
    print(word*freq)
    
call= func('tim',5)#timtimtimtimtim

def func(word,freq=2):
    print(word*freq)
    
call= func('tim')#timtim

call= func(10) #20

#multiple optional parameters

def func(word, add=5, freq=1):
    print(word*(freq+add))
    
call = func('hello') #hellohellohellohellohellohello

call = func('hello',0) #hello

call = func('hello',5,0) #hellohellohellohellohello

### Class example

class car(object):
    def __init__(self,make,model,year,condition='New',kms=0):
        self.make = make 
        self.model = model 
        self.year = year
        self.condition = condition 
        self.kms = kms 
        
    def display(self,showAll=True):
        if showAll:
            print(f"This car is a {self.make} {self.model} from {self.year}, it is {self.condition} and has {self.kms} kms")
        else:
            print(f"This car is a {self.make} {self.model} from {self.year}.")
            
whip = car('Ford','Fusion',2012)
whip.display(False)

