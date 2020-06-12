
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
#web
import webbrowser
webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://www.youtube.com/watch?v=CMNry4PE93Y")
help(webbrowser)
#time package (execution of code)
import time
start = time.time()
print("Program Start")
time.sleep(5)
print("Program End. The total execution time was {} sec.".format(time.time() - start))
#datetime
from datetime import datetime
print(datetime.today())
print("Day: {}\nMonth: {}\nYear: {}".format(datetime.today().day, datetime.today().month, datetime.today().year))
if datetime.today() > datetime(datetime.today().year, 7, 4):
    days_until = (datetime(datetime.today().year + 1, 9, 4) - datetime.today()).days
    age = (datetime.today().year + 1) - 1998
else:
    days_until = (datetime(datetime.today().year, 9, 4) - datetime.today()).days
    age = datetime.today().year - 1998
print("There are {} days left until My birthday. I will be {} years old.".format(days_until, age))
# OS Pacakge
import os
print(os.getcwd())
print(os.cpu_count())
print(os.getlogin())
