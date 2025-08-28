#Implement a program to generate Fibonacci numbers up to n terms using generators.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n=int(input("Enter the value for n:"))
print(list(fibonacci(n))) 
