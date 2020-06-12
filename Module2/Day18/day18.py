
#display all built in functions in package
from turtle import Turtle

for func in dir(__builtins__):
    print(func)
#call that function ( need understand
import random
num = random.randint(0, 100)
for i in range(0, 100):
   try:
       guess = int(input("Guess a number between 0 and 100: "))
   except:
       print("Please enter a valid integer between 0 and 100.")
       break
   if guess == num:
       print("{} is the correct value. You win.".format(guess))
   elif guess < num:
       print("{} is lower than the value. You have {} tries left.".format(guess, 2 - i))
   elif guess > num:
       print("{} is higher than the value. You have {} tries left.".format(guess, 2 - i))
   else:
       print("Something went wrong.")
#turtle - turle art
import turtle
angle = 91
turtle.showturtle()
turtle.shape("turtle")
for x in range(100):
    turtle.forward(x)
    turtle.left(angle)