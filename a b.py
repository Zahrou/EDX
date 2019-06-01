



def recursivemul(a, b):
    if b == 1:
        return a
    else:
        return a + recursivemul(a, b-1)

print(recursivemul(3, 4))

def factorial(i):
    if i == 1:
        return i
    else:
        return i * factorial(i-1)

print(factorial(25))
