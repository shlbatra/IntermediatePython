#use functions defined in math_functions in test.py script here
import math_functions #as in same folder, have access to functions here 

print(math_functions.get_average([1,3,4,5,6]))
ht={"hi":1, "tim":6}
print(math_functions.max_value(ht))
'''
Above approach not good - not cohesive as we want to put similar things together. ex. guess number - all methods in same class and all methods cohesive too
Mathfunctions - 2 diff purpose - 1 for hash table and other for list so create diff modules for both files
Both files can have same function names as well to keep function names consistent across modules.
'''
print("\n\n")
import ht_functions as h
import list_functions 

print(list_functions.get_average([1,3,4,5,6]))
ht={"hi":1, "tim":6}
print(h.get_max(ht))

'''
Import specific function directly

'''
print("\n\n")
from ht_functions import get_max as ht_get_max,get_min #rename function in this file scope to ht_get_max
from list_functions import get_max,get_min  

ht={"hi":1, "tim":6}
#print(get_max(ht))  #run in list_functions so error out. Most recent import used so list_functions used. Namespace for program used most recent version 
#fix above issue using alias

print(ht_get_max(ht))

'''
Create Package - ht and list functions seperate into package and use a package
Package is a folder with python modules 
To create a module, put a __init__ file in folder -> tell python that initializes folder as package - so import utils to get both 
ht_functions and list_functions. Cohesive folder for 2 modules that are similar act on list or hash tables. Functions just do 1 thing. 
'''

print("\n\n")
import utils 
from utils import ht_functions as ah, list_functions as al  #organize things in much better way 


ht={"hi":1, "tim":6}
print(ah.get_max(ht))
print(ah.get_keys(ht))