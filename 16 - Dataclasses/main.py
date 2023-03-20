from dataclasses import dataclass, field

class BlogPost:
    def __init__(self,user:str):
        self.user=user
    
    def __repr__(self):
        return f'BlogPost(user={self.user})'
    
b1=BlogPost('Jim')
print(b1) #O/P = BlogPost(user=Jim)

print("\n\n\n")
#Using dataclass approach

@dataclass(frozen=True)  #use it as decorator for class, freeze values after instantiation for instance
#,kw_only=True only added from Python 3.10
class BlogPost:
    user:str  #attributes for class, assign them to self object and design repr class by itself
    content:str=field(repr=False) #using field exclude from dataclasses repr method
    expiry: int=24 #Presented by hours
    likes:int = 0#by default, 0 likes, default value attributes in last position in class
    
#force users to provide keyword so know which argument has value
b1=BlogPost(user='Jim',content='This is the first post. Welcome',expiry=46) #dataclasses.FrozenInstanceError: cannot assign to field 'user'
#b1.user="Paul" -> attributes frozen so cannot change after instantiation
print(b1)
#b1.likes+=1 #cannot make this change with dataclass, effects Encapsulation OOP principle so use 
# a method that increase likes within class. 
# ex. def add_like(self,n): self.likes+=n
# b1.add_like(3)

