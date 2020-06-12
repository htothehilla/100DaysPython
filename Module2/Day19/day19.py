
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