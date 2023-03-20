#Counter
import collections 
from collections import Counter

#parameter can be any collection datatype ex. list, set, dict, tuple 
c=Counter('gallad')    #count characters in string as its own object called Counter 
print(c)
print(c.most_common(1))
c=Counter(['a','a','b','c','c']) #
print(c)
c=Counter({'a':1,'b':2}) # 
print(c)
c=Counter(cats=4,dogs=7) #
print(c)
#Reference specific item 
print(c['cats'])
print(c['pet']) #if key not in counter then get 0 not error. In dictionary, you will get an error if the key is not in dictionary

print(list(c.elements())) #print all elements with number of occurances as value

print(c.most_common(1))

#Another example 
c = Counter(a=4,b=2,c=0,d=-2)
d=['a','b','b','c']  #list / dict / counter / set / tuple 

#subtract counter objects 
c.subtract(d)
print(c)
#add counter objects
c.update(d)
print(c)

#clear - remove all counts, empty counter 
c.clear()
print(c)

#add counter using + sign , subtract using - sign 
c = Counter(a=4,b=2,c=0,d=-2)
d=Counter(['a','b','b','c'])
#if element count <= 0 not shown in output after the operations below 
print(c+d)
print(c-d)   

#Intersection - minimum elements in each list 
print(c&d)
#Union - maximum elements in each list
print(c | d)

