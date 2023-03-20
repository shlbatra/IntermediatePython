- Collections -> allow to store diff datatypes without using loops. 

- Containers -> data type store multiple tyoes.
Ex - 
- List
- Set
- Dict
- Tuple - immutable 

# Types in Collections module 
- counter
- deque
- namedTuple()
- orderedDict
- defaultDict

- Syntax, c = Counter(<container>). To refer to specific element, c[key]
- Common Functions used 
    - c.most_common(<number>)
    - c.subtract(container) -> subtract container from c
    - c.update(d) -> add container to c
    - c+d  -> Both c and d are counters, output will not have key with <= values.
    - c-d  -> Both c and d are counters, output will not have key with <= values.
    - c & d  -> Both c and d are counters,return minimum elements in each counter,  output will not have key with <= values.
    - c | d  -> Both c and d are counters,return maximum elements in each counter,   output will not have key with <= values.