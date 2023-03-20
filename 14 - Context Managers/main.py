'''
Problem with code below -
Issue happens when write line errors out - then open file and not closed it
  
'''
file = open("14 - Context Managers/file.txt","w")
file.write("hello") #error here then file open and not closed. Then someone else - shared resource not access file.
file.close()

#How make sure reach file.close no matter what happens between open and close -> use try and catch exception as a solution
file = open("14 - Context Managers/file.txt","w")
try:
    file.write("hello") #error here then file open and not closed. Then someone else - shared resource not access file.
finally:    
    file.close()

#Alternate way - use context manager 

with open("file.txt","w") as f: #same as try and finally code above
    f.write("hello")
    
#open method defines what do when use as context manager when enter and exit
#open file and return as file object when enter context manager with keyword 
# then do write/print/whatever
# when steps done regardless exception - call exit method - code to close file properly
#hidden way that when do one operation then do finish operation regardless of what happens in between. 
#locking and unlocking shared memory

#Wite own context manager - 
#functions inside context manager - use as usually would if not context manager . 

class File:
    def __init__(self,filename,method):
        self.file=open(filename,method)
        
    #first thing that happens in Context Manager, with something as f -> something call enter and return stored in f
    def __enter__(self): #dundar methods called in special way for context manager 
        print("Enter")
        return self.file 
    
    def __exit__(self,type,value,traceback): #called in special way from python using context manager syntax,
        #handles exception here by calling exit method with exception  
        print(f"{type}, {value}, {traceback}") #get exception details through these parameters
        #Handle exception - if determine is all good and let the program run using return True
        print("Exit")
        self.file.close()
        if type == Exception:
            return True #be careful if exception need to handle using 
    
        
with File("14 - Context Managers/file.txt","w") as f: #allowed to do this as we have defined enter and exit dundar method:
    print("Middle")
    f.write("Hello")
    raise Exception() #raised exception - still got to exit method as we had already entered. we can handle exception inside exit method as it is sent to the exit method
    #File ExistsError() -> this will crash the python program
    
#create context managers using generators & decorators 
# get decorator from contextlib that allows to decorate a generator that becomes context manager 
import contextlib 
from contextlib import contextmanager

@contextmanager #decorator turns the generator object below into context manager
def file(filename,method):
    print("enter1")
    file=open(filename,method) #create file object as enter 
    yield file # yield where called from 
    file.close() #when function resumes again then close function, handle exceptions here
    print("exit1") 
    
with file("14 - Context Managers/file.txt","w") as f:
    print("middle")
    f.write("hello")

#locks in thread - shared memory - memory locks 
#x -> 2 diff threads - create memory lock, so one thread wait till lock available before access object. so thread unlock resource before changing it





        