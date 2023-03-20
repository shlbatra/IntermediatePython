# Example 1 - Common Design Mistakes
#Program Goal, print a list of words delimited by commas

#Soln 1 - What's wrong ?
'''
1. design code for flexibility - add another word to list and output not change so not designed flexibility
2. Scalabily - change delimiter - then make change at multiple places. hardcode variables -> show up at many places, change every aspect - lead to human error, 
'''
list_of_words = ["hello","yes","goodbye","last"]
print(list_of_words[0] + "," + list_of_words[1] + "," + list_of_words[2] + "," + list_of_words[3])

#Soln 2
print("\n\n")
'''
Whats wrong ?
1. 4 -> still hardcoded - how many elements in list -> need to change to len(list_of_words), and i!= len(list_of_words)-1
'''
list_of_words = ["hello","yes","goodbye","last"]
to_print= ""

for i in range(4):
    to_print += list_of_words[i]
    if i != 3:
        to_print += ","
print(to_print)

#Soln 3
print("\n\n")
'''
Flexible program so works for diff variations of problem 

'''

list_of_words = ["hello","yes","goodbye","last"]
to_print= ""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words)-1:
        to_print += ","
print(to_print)

#Soln 4
print("\n\n")
'''
Much better -
1. Flexible as work for any words
2. Change delimeter at one place only 
'''
list_of_words = ["hello","yes","goodbye","last"]
print(",".join(list_of_words))

#Soln 4
print("\n\n")
'''
BEST -
1. Now only change constant -> used through out problem. Reuse delimeter variable anywhere in program now
Flexible, Scalable and adapt to changing problem that happens in large problem/codebase -> code works when things change around. 
'''
delimeter=","
list_of_words = ["hello","yes","goodbye","last"]
print(delimeter.join(list_of_words))
print(delimeter.join(list_of_words))




