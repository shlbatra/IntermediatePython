
def func(x):
    return x+5

print(func(2))

#Alternate way using lambda function

func2 = lambda x:x+5   #   lambda <multiple parameters>: <expression to return>

print(func2(2))  

#use lambda function inside another function 

def func(x):
    func2 = lambda x:x+5 
    return func2(x) + 10 

print(func(2))

#use lambda function with multiple parameters 

func3 = lambda x,y=4: x+y 
print(func3(5,5))
print(func3(5))

#lambda with map and filter functions 

a=[1,2,3,4,5,6,7,8,9,10]

# newList = list(map(func,a))   -> replace func with lambda function here 
# func = lambda x:x+5
newList =list(map(lambda x:x+5,a))
print(newList)

newList=list(filter(lambda x:x%2==0,a))
print(newList)
