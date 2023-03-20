def add7(x):
    return x+7

def isOdd(x):
    return x%2 !=0   #return True/1/'hi' gives all values in filter

a = [1,2,3,4,6,7,8,9,10]

#Implement with filter function
b=list(filter(isOdd,a))  #takes function and iterable list/string, Pass each element to function and return to b list only the ones 
#that return true 
print(b)

#Implement with map function on filtered list 

#c=list(map(add7,b))
c=list(map(add7,filter(isOdd,a)))
print(c)