# good example - https://www.youtube.com/watch?v=Uh2ebFW8OYM
# always import os
import this
import os

print(os.getcwd())
os.chdir('./Module2/Day19')

zen = ""
for letter in list(this.s):
    if letter in list(this.d.keys()):
        zen += this.d[letter]
    else:
        zen += letter
print(zen)
# Additionally, the .readline() method produces the entire line of the file or a
# specific number of characters specified within the parentheses
with open('declaration.txt', 'r') as d:
    print(d.readline())
    print(d.readline(25))
d.close()

with open('farewell.txt', 'r') as d:
    for lines in d:
        print(lines, end='')
d.close()

# The file= option within the print statement allows the content to printed to the open file.
# Since a file with an active append status cannot be read
# Read the file in the original state.
print("{:=^50}\n".format(" BEFORE APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

# Appending action
with open('constitution.txt', 'a') as c:
    print('\n', file=c)
    with open('billofrights.txt', 'r') as b:
        for lines in b:
            print(lines, end='', file=c)
    b.close()
c.close()

# Confirmation of successful appending.
print("\n\n{:=^50}\n".format(" AFTER APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

os.rename("constitution.txt", 'constitutionBillOfRights.txt')
