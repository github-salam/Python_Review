# getting started
#print("hello world")

# system modile
# import sys
# print(sys.version)

# indentation
# if 6 > 5:
#     print("6 is greater than 5")  # this line containing some white space at the beggining which is consider as indentation

# variable declaration -> when you assign value to it
# var = 59
# print(var)

# comment is already used once

"""
this 
could 
be used as multiline comment
"""
"""
type_casting = str(90)
print(type(type_casting))
"""

# x,y,z = "salam", 45, "kalam" # assgining multiple values in a single line
# print(x,y,z)

# x = y = z = "same values to multile variables\n"
# print(x,y,z)

# unpack values
# li = [23,45,67,89,"kuttish", "motu"]

# a,b,c,d,e,f = li
# print(a,b,c,d,e,f)

# create outside of a function is known as global variable
# k = 5
# def example():
#     k = "updated"
#     print(f"i am testing global variable k is {k}")
# example()
# print(f"gloabl {k}")

# fahim = 7
# def key():
#     global fahim
#     fahim = 6
# key()
# print(fahim)


# data type
# print(type(5))
# print(type(5.5))
# print(type("string"))
# print(type(5+9j))
# print(type(True))
# print(type({4,5,6}))
# print(type(["salam",8,9.8,"a"]))
# print(type({"name":"salam","age":23}))
# print(type(frozenset({4,3,5})))

# random module
import random
print(random.randrange(1,20))