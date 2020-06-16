#custom functions

def hello():
    return "Hello World!"

print(hello())
#rule of fun- Functions are used to reduce code duplication.
# If a block of code is used more than twice, it's best to turn it into a function.

#
def even(a):
    while a % 2 != 0:
        a *= 2
    return a

for x in [0, 35, 2, 107, 254]:
    if x == even(x):
        print(f"{x} is an even number.")
    else:
        print(f"{x} first becomes an even number when it's multiplied by 2 to become {even(x)}.")

# Creating the same output without using a function. While this is still readable and easy to understand for the simple
# case, more complex problems quickly become confusing.
for x in [3, 35, 2, 107, 254]:
    if x % 2 == 0:
        print(f"{x} is an even number.")
    else:
        y = x * 2
        print(f"{x} first becomes an even number when it's multiplied by 2 to become {y}.")
#declare all functions at the beginning
def pythag(a):
    c = (a ** 2 + even(a) ** 2) ** .5
    return c

x = int(input("Please provide an integer."))
print(f"Function output: {pythag(x)}.")

if x % 2 == 0:
    man_a = x
    man_b = x
else:
    man_a = x
    man_b = x * 2
print(f"Manual Calculation: a = {man_a}, b = {man_b}, c = {(man_a ** 2 + man_b ** 2) ** .5}")
#Complex functions can be created to completed tasks like matrix addition.

def matrix_add(m1, m2):
    if len(m1) != len(m2):
        raise ValueError("Given matrices are not the same size.")
    for i in range(0, len(m1)):
        if len(m1[i]) != len(m2[i]):
            raise ValueError("Given matrices are not the same size.")
        for j in range(0, len(m1[0])):
            m1[i][j] = (m1[i][j] + m2[i][j])
    return m1

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(matrix_add(matrix1, matrix2))
#docstrings : It is critical that custom functions include docstrings.
# This adds built-in documentation for the function which assists the user in correct implementation and improves understanding of functionality.

def matrix_mult(m1, m2):
    """
    This function accepts two matrices of any, but equal size and multiplies the values at each identical index.

    e.g.
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    returns: [[2, 2], [0, -4]]

    :param m1: A list of lists (i.e. a matrix). Can only contain numeric values.
    :param m2: A list of lists (i.e. a matrix) of the same size as m1. Can only contain numeric values.
    :return: matrix1 * matrix2
    """
    if len(m1) != len(m2):
        raise ValueError("Given matrices are not the same size.")
    for i in range(0, len(m1)):
        if len(m1[i]) != len(m2[i]):
            raise ValueError("Given matrices are not the same size.")
        for j in range(0, len(m1[0])):
            m1[i][j] = (m1[i][j] * m2[i][j])
    return m1

print(matrix_mult.__doc__)
print(help(matrix_mult))
# guidance on expected variable type

def multi_out(a: int) -> [int, float]:
    """
    Takes an integer, adds two, and then calculates the hypotenuse based on the two previous values.
    :param a: int
    :return: b: int (a + 2)
             c: float (hypotenuse of a and b)
    """
    b = a + 2
    c = (a ** 2 + b ** 2) ** .5
    return b, c

a = 5
b, c = multi_out(a)
print(f"Two more than {a} is {b} and the hypotenuse of those two is {c:.2f}.")