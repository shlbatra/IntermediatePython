"""
Hash Table Functions (dictionary)  
"""

def get_keys(ht):
    return ht.keys()

def has_key(ht,key):
    return key in ht

def get_max(ht):
    """
    Assume all values are int
    """
    mx=float("-inf")
    
    for k, v in ht.items():
        if v > mx:
            mx=v
    return mx 

def get_min(ht):
    """
    Assume all values are int
    """
    mn=float("-inf")
    
    for k, v in ht.items():
        if v < mn:
            mn=v
    return mn