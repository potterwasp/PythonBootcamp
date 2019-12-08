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

