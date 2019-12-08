# -*- coding: utf-8 -*-
"""-------------------------------------------------------------------------
Strings are used in python to record text informations.Strings in python are 
actually a sequence. 
Properties of strings :
    1. Immutable :
    2. Ordered : Being an ordered sequence, stringsrecord element position or 
    order of insertion.
    
---------------------------------------------------------------------------"""

text = "Hello World!"
print(text)


# immutable: the following will fail with error : 'str' object does not support  
# item assignment

''' text[2]="z"'''

''' printing the length of a string '''
print(len(text))



'''--------------------------------------------------------------------------
    string indexing  and slicing

    We know that strings are a sequence so Python can use indexes to access 
    parts of the sequence.    

----------------------------------------------------------------------------'''

print(text[2])  #prints l or the third character of a string



''' we can use the ":" operator to slice the strings '''

#1.  Grab everything from the nth character to the end of the string which is 
#    given by len function

print(text[2:])

#2. Grab everything between nth character to mth character using [n:m]

print(text[2:8])

#3. Grab everything between nth to mth character using step(skipping)
''' We can also use index and slice notation to grab elements of a sequence by 
a specified step size (the default is 1). For instance we can use two colons in 
a row and then a number specifying the frequency to grab elements. For example:
'''    

print(text[0:12:1]) #prints every character

print(text[0:12:2]) #prints every second character 

print(text[0:12:3]) #prints every third character 

#another way

print(text[::1]) #grabs everything in steps of 1

print(text[::2]) #grabs everything in steps of 2

print(text[::3]) #grabs everything in steps of 3

#4. grab everything upto the third index 

print(text[:3])

#5. Grab everything 

print(text[:])

''' We can also use negative index '''
#1. Grab the last index 

print(text[-1])

#2. Grab everything but the last index

print(text[:-1])

#3. print in reverse order

print(text[::-1]) #grabs everything in reverse order in steps of 1

print(text[::-2]) #grabs everything in reverse order in steps of 2

print(text[::-3]) #grabs everything in reverse order in steps of 3


#4. Concatention

text2 = text + " concatenation "
print(text2)

#5. Reassignment: we can reassign the text altogether
text = text + " concatenate me ! "
print(text)

#6. Multiplication of characters to create repeated occurance
letter = "z"
print(letter*10)

'''---------------------------------------------------------------------------
    Built in string functions
    Objects in python usually have built in funtions. The format is 
    object.method(Parameters)
   -------------------------------------------------------------------------'''

#1. Change to uppercase 
print(text.upper())

#2. Change to first letter to upper
text2 = "first lower"
print(text2.capitalize())

#3. change to lowercase 
text2 = "ALL CAPS"
print(text2.lower())

#4. Split a string with a blank space 
print(text.split())

#5. Split a string at the occurance of a character
print(text.split("W"))
































