content = ["Wayne is the toughest guy in Letterkenny.", list(range(0,101,10)), ("Wayne", "Dan", "Katy", "Daryl"), 10.4]
print(content)

for word in content:
    if type(word) == tuple:
        print()
    elif type(word) == list and int:
        word = int(word) - 10
        word = float(word) - 20
        print()
    elif type(word) != str or int or tuple:
        print("stop")
    else type(word) ==
        content = content + "Allegedly"
        print()

# Create a program that iterates through a list of values.

# If the object is immutable, print the type and advance to the next step.

# If the object is mutable and a string, add "Allegedly" to the end.

# If the object is mutable and a number, take 10 (for an int) to 20 (for a float) percent off,
# print the new value, and overwrite the value in the existing position.

# If an object is not a string, number, or tuple,
# end the program immediately while displaying the object and the type for review.