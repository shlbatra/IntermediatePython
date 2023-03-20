- Program has finite amount of memory and when run program, its loaded in memory, variables and lists stored in memory - fast to retreive 
and store data. Work in RAM so limited to RAM on our computer so possible to fill up all RAM.
- T solve a problem of processing a huge list where get memory error, we can look at one value at a time and not store the entire sequence of numbers if not reqd.
- Generator is used as much better optimized way for infinite length of sequence
- Generator keep track of the internal state for next number we generate. Store last value only and generate next one accordingly
- Use keyword yield - that pause after returning the value and stores the internal state of the returned variable. Yield is a pause and return is a stop for execution. As we store the internal state of variables only, so we dont get out of memory errors when using yield.
- next function on generator gets next value till yield keyword last value
- Complex generators can have start variables inside , yield basically pauses execution - ex. loop through 5 times and later continue looping when reqd. 
- Complex concepts on generator -> close and stop generator, set values to generator 