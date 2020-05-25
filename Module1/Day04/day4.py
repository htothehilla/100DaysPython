#Variables need to start with a letter or an underscore.
# Numbers can be used in the variable name as long as it is not the first character.
# Additionally, python is case sensitive,
# so the same word can store multiple items as long as the casing differs.
greeting = "Hello"
_name = "General Kenobi."
Greeting = "There"
_bestLine_ep3_ = "You are a bold one."
# Using string concatenation:
print(greeting + " " + Greeting + "\n\t" + _name + " " + _bestLine_ep3_)
# Using string replacement:
print(f"{greeting} {Greeting}\n\t{_name} {_bestLine_ep3_}")
# Variables can also store numeric values
released = 2005
print("Revenge of the sith was release on May, "+ str(released)+".")
print(f"Revenge of the sith was released on May 4,{released}")
#Variables are commonly used in arithmetic operations
a = 3
b = 4
c = (a ** 2 + b ** 2) ** .5
print(f"Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {a} and b = {b}, then c = {c}")
#You can test for contents in a variable.
# If the test results True, then the tested condition is in the variable.
# Otherwise, the test returns False.
film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())
#Python variables get their type with the data that is stored.
# Unlike other programming languages, you do not declare a type for the variable.
# Additionally, the same variable can be overwritten with new data and a different type.
# This should be taken into account when creating python programs.
var = "Variables are mutable"
type(var)
var = 3
type(var)
var = 3.5
type(var)
# If the variable contains a numeric value, it can be converted to an integer type with the int() function.
var = int(var)
type(var)
# The variable can be converted to a string with the str() function regardless of the contents.
var = str(var)
type(var)
# If the variable contains a numeric value, it can be converted to an float type with the float() function.
var = float(var)
type(var)
var = True
type(var)
