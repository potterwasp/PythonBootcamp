#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
String formatting
Created on Mon Dec  9 00:27:41 2019

@author: rockchar
"""

#1. Using the format method we can format the string 

print("This is an example text ! {} text will be inserted.".format("missing"))
# same thing with a text variable
text = "This is an example text ! {} text will be inserted here."
formattedText = text.format("missing")
print(formattedText)

#2. Formatting using place holders

print("This is where %s will be inserted"%'something')

print("Example2 where %s will be inserted"%("something"))

print("We are going to %s some %s text here"%("insert","more"))

#3. Formatting using place holders and variable names

x,y="insert","more"
print(x,y)

print("We are going to %s some %s text here"%(x,y))


''' FORMAT CONVERSION METHODS ----------------------------------------------
In python there are two methods %s and %r that are used to convert a python
object to a string using methods str() and repr()
repr() delivers the string representation of the object using quotes and any
escape characters.
In addition to %s,%r we have %d,%f for decimal and float
If %s encounters a number it will convert it to a string as it is including 
integers and float.
If %d encounters a number, it will first convert to integer without rounding 
and then convert to string
----------------------------------------------------------------------------'''

#1. Using %s and %r
print("He said his name was %s"%("Fred"))
print("He said his name was %r"%("Fred"))

#2. Escape characters using %s and %r
print("This is a tabbed %s"%("\t statement"))
print("This is a tabbed %r"%("\t statement"))

#3. Numbers using %s and %d and %f
print("Print a number %s"%12.345)
print("Print a number %d"%12.345)
print("Print a number %f"%12.345)




'''PADDING AND PRECISION OF FLOATING POINT NUMBERS-----------------------------
    Floating point numbers use the format %x.yf where x is the minimum number 
    of characters the string should contain. If the number does not contain as
    many digits specified by x, the remaining space is padded with whitespace.
    
    If x is smaller than the number of digits before the decimal point then it
    is ignored.
    
    y is the number of precision digits after the decimal point. If there are 
    not enough precision digits then it is padded with 0. Lets see 
    some examples.
----------------------------------------------------------------------------'''

number = 123456.7891011

#1. Converts to an integer first
print("Example of Padding and precision %d"%number)

#2. Float representation without padding and precision specifiers
print("Example of Padding and precision %f"%number)


#3. Float representation with smaller value of x and y 
print("Example of Padding and precision %2.3f"%number)

#4. Float representation with higher value of padding and precision specifiers

print("Example of Padding and precision %100.100f"%number)

''' Explaination _
#NOTE: the output of the above is 123456.7891011000028811395168304443359375
#      000000000000000000000000000000000000000000000000000000000000000000
# We can see that there are some more digits that we did not specify. This is 
# because how python interprets the numbers.


Stop at any finite number of bits, and you get an approximation. 
On most machines today, floats are approximated using a binary fraction with 
the numerator using the first 53 bits starting with the most significant bit 
and with the denominator as a power of two. In the case of 1/10, 
the binary fraction is 3602879701896397 / 2 ** 55 which is close to but not 
exactly equal to the true value of 1/10.

Many users are not aware of the approximation because of the way values are 
displayed. Python only prints a decimal approximation to the true decimal value 
of the binary approximation stored by the machine. 
On most machines, if Python were to print the true decimal value of the binary 
approximation stored for 0.1, it would have to display:
    0.1000000000000000055511151231257827021181583404541015625

That is more digits than most people find useful, so Python keeps the number 
of digits manageable by displaying a rounded value instead
Just remember, even though the printed result looks like the exact value of 
1/10, the actual stored value is the nearest representable binary fraction.

The problem is easier to understand at first in base 10. Consider the fraction 
1/3. You can approximate that as a base 10 fraction:

0.3
or, better,

0.33
or, better,

0.333
and so on. No matter how many digits you’re willing to write down, the result
will never be exactly 1/3,but will be an increasingly better approximation of 1/3.

In the same way, no matter how many base 2 digits you’re willing to use, 
the decimal value 0.1 cannot be represented exactly as a base 2 fraction. 
In base 2, 1/10 is the infinitely repeating fraction

0.0001100110011001100110011001100110011001100110011...
Stop at any finite number of bits, and you get an approximation.
____________________________________________________________________________'''






































