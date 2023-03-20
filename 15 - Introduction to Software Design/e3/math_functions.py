"""
LIST Functions    
"""

def get_max(lst):
    mx = float("-inf")
    
    for num in lst:
        if num > mx:
            mx = num 
            
    return mx 

def get_min(lst):
    mn = float("inf")
    
    for num in lst:
        if num <mn:
            mn = num
    
    return mn

def get_average(lst):
    return sum(lst) / len(lst)

def get_mdeian(lst):
    lst=sorted(lst)
    
    if len(lst)%2==0:
        return (lst[(len(lst)/2)-1] + lst[(len(lst)/2)]) / 2
    else:
        return lst[(len(lst)-1)/2]
    
"""
Hash Table Functions (dictionary)  
"""

def has_key(ht,key):
    return key in ht

def max_value(ht):
    """
    Assume all values are int
    """
    mx=float("-inf")
    
    for k, v in ht.items():
        if v > mx:
            mx=v
    return mx 

def min_value(ht):
    """
    Assume all values are int
    """
    mn=float("-inf")
    
    for k, v in ht.items():
        if v < mn:
            mn=v
    return mn


