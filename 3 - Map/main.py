
li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

#Bad Way 
newList = []
for x in li:
    newList.append(func(x))
    
print(newList)

#Map method - shorten 

print(list(map(func,li))) #map takes two arguments -> function and list to apply the function 

#Use list comprehension with filter condition

print([func(x) for x in li if x%2==0])

#Apply two methods 

#def func(x):
#    return func2(x**x)


 