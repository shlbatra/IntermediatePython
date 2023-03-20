'''
Program has finite amount of memory and when run program, its loaded in memory, variables and lists stored in memory - fast to retreive 
and store data. Work in RAM so limited to RAM on our computer so possible to fill up all RAM.

'''

#x = [i**2 for i in range(1000000000000)] #generate sequence of all squares and print them out

#for el in x:   #get memory error
#    print(el)  
    
#here processing one value at a time so dont need list to loop through 
#for i in range(1000):
#    print(i**2)
    
#Use generator to fix above issue - look at one value at a time and not store the entire sequence of numbers if not reqd

#code Generator pattern below -
print("\n\n")
class Gen:   #generate sequence to numbers till N
    def __init__(self,n):
        self.n=n
        self.last=0#last number generated square
        
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last == self.n:
            raise StopIteration() #error that we cannot go any further 
        
        rv=self.last**2
        self.last +=1
        return rv
        
g = Gen(10001)
#Here keep track of the interna state for next number we generate. Store last value only and generate next one accordingly 
#while True:
#    try:
#        print(next(g))  #__next__ allows to call next method on g object 
#    except StopIteration:
#        break
print("\n\n")     
#####################################################
## Create this class as a generator using yield keywrd -> returns value for current iteration and stops after that and keeps track of our last number - internal state stored 
#yield is a pause and return is a stop for execution

# create generator with function gen with 1M, then loop through this. run the loop till se yield. pauses and then loop again and then call again
# pausing so doesnt use memory and give memory out error. 
def gen(n):
    for i in range(n):
        yield i**2
        
g = gen(10001)

#for i in g:
#    print(i)
    
#print(next(g)) #next function on generator gets next value till yield keyword last value
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))


def gen(n):
    yield 1
    yield 10
    yield 100
    yield 1000
    yield 10000
    yield 10
    
g = gen(9000)

#print(next(g)) #once cross the total max number of yeild and if next called, get stop iteration error - no more keyword yield so nothing more to return
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))

#compare size in memory for generator object and list 

import sys 

x=[i ** 2 for i in range(1000000)]
g = gen(1000000)
#get number of bytes used by object 
print(sys.getsizeof(x)) #8448728
print(sys.getsizeof(g)) #112

#much better optimized way for infinite length of sequence
#close and stop generator, set values to generator - advanced review 
# complex generators - start variables inside , yield pause execution - loop through 5 times and later continue looping when reqd.  


        

    