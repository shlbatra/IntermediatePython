- shared memory, shared resources, locking, unlocking, 
- Context manager -> hidden way that when do one operation then do finish operation regardless of what happens in between.
- Ex. when writing to a file, Issue happens when write line errors out - then open file and not closed it. 
- So, one way of doing it is using try and catch. Ex below -
    file = open("14 - Context Managers/file.txt","w")
    try:
        file.write("hello") #error here then file open and not closed. Then someone else - shared resource not access file.
    finally:    
        file.close()
- Alternate way to use context manager -
    with open("file.txt","w") as f: #same as try and finally code above
        f.write("hello")
- open method defines what do when use as context manager when enter and exit, open file and return as file object when enter context manager, 
then do write/print/whatever, when steps done regardless exception - call exit method - code to close file properly
- Alternate method - create your own class with __enter__ and __exit__ dundar methods. Exception can be handled with type,value,traceback arguments passed to __exit__ method 
- Alternate way is to create context managers using generators & decorators. Basically, get decorator from contextlib that allows to decorate a generator that becomes context manager. Python module used - from contextlib import contextmanager
