# Recursive functions are ones that call on themselves to produce additional results
#factorial =  A factorial is the product of all numbers from 1 to N
# The recursion function determines the highest numerical value in each iteration and
# adds it to the list of items to multiply

def factorial(n) -> int:
    if n < 0:
        print("n must be a positive number. {} is an invalid response.".format(n))
        exit(code=1)
    if n in (0, 1):
        return 1
        return factorial() * n

n = int(input("Provide an integer for factorial calculation: "))

soln = 1
for i in range(0, n + 1):
    if n < 0:
        print("n must be a positive number. {} is an invalid response.".format(n))
        break
    if i in (0, 1):
        soln = 1
        continue
    soln *= i

print("""{}!Recursion Results: {} Loop Results: {}""".format(n, factorial(n), soln))

#comparision of loops and recursions

import time

def fibonacci(n):
    """
    The Fibonacci sequence is a list of numbers where the subsequent number is the sum of the previous two.
    :param n: The number of items requested for the Fibonacci sequence.
    :return: The Fibonacci number at position n
    """
    if n <= 0:
        raise ValueError("The number must be greater than zero.")
        exit(code=1)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

fib_length = int(input("How long do you want the Fibonacci sequence? "))
loop_start = time.time()
# List contains the static first two items in the Fibonacci sequence.
output = [0, 1]

if fib_length < 2:
    if fib_length == 2:
        print("Fibonacci Sequence with Length: {}\n{}".format(fib_length, output))
    elif fib_length == 1:
        print("Fibonacci Sequence with Length: {}\n{}".format(fib_length, output[0]))
    else:
        print("The range of the Fibonacci sequence must be greater than zero.")
        exit(code=42)

for i in range(1, fib_length):
    output.append(output[i-1] + output[i])

print("Loop Performance Test")
for k in range(0, len(output) - 1):
    print("{}: {}".format(k + 1, output[k]))
loop_end = time.time()
loop_sec = loop_end - loop_start
print("Loop Execution Time: {} sec".format(loop_sec))

print("")
print("=" * 100)
print("")

print("Recursion Performance Test")
recursion_start = time.time()
for n in range(1, fib_length + 1):
    print("{}: {}".format(n, fibonacci(n)))
recursion_end = time.time()
recursion_sec = recursion_end - recursion_start
print("Recursion Execution Time: {} sec".format(recursion_sec))
print("=" * 50)
print("The recursive function took {} sec longer than the loop.".format(recursion_sec - loop_sec))

#computer has to remember
#This can be remedied by using memoization.
# Memoization is simply caching the previous values so it can be accessed in subsequent calls.

import time

cache = {}

def fibonacci(n):
    """
    The Fibonacci sequence is a list of numbers where the subsequent number is the sum of the previous two. Memoization
    is added as an enhancement (in the form of a dictionary) to efficiently record and retrieve previously calculated
    values of the Fibonacci sequence.
    :param n: The number of items requested for the Fibonacci sequence.
    :return: The Fibonacci number at position n
    """
    # Looks for a cached value and returns it if found.
    if n in cache:
        return cache[n]

    if n <= 0:
        raise ValueError("The number must be greater than zero.")
        exit(code=1)
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    # Add the result to the cache
    cache[n] = result
    return result


recursion_start = time.time()
for n in range(1, fib_length + 1):
    print("{}: {}".format(n, fibonacci(n)))
recursion_end = time.time()
recursion_sec = recursion_end - recursion_start
print("Recursion Execution Time: {} sec".format(recursion_sec))

#hard cap on recurssion functions

import sys
print(sys.getrecursionlimit())

#Additionally, the recursion limit can be manually set using the
# .setrecursionlimit() function based on the program limitations.
import sys
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
