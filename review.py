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
# import random
# print(random.randrange(1,20))

# # type casting
# print("int to float" , f"{float(5)}")
# print("float to int", f"{int(5.9)}")
# print("float to string",f"{str(8.9)}")
# # means we can use constructor for casting one to another data type!!

# Python String -> anything inside single or double quote 

print('hello "world" with quote clearation!')

multiline_string = """Lorem Ipsum is simply dummy text of the printing and typesetting 
industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"""

print(multiline_string, multiline_string[-1])

for l in range(len(multiline_string)):
    print(multiline_string[l], end=" ")
    if l == 10:
        break

print("\n\n")

if 'typesetting' in multiline_string:
    print("Yes it is in the string!")
if 'salam' not in multiline_string:
    print("it is not in the string!")

# string slicing
print(multiline_string[(len(multiline_string)-5):])

# string formatting with modifier

print(f"hello {2000:.4f}")

# small project on string modification

name = input("Enter you name : ").strip().capitalize()
print("Hello" + " " +name + " how are you?!".upper())

# easy peasy :)