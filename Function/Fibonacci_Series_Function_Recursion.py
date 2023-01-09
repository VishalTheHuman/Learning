# Python Program to print ’nth’ terms of the Fibonacci Sequence.(use recursive function).

def fib(terms):
    if (terms ==2 or terms == 1):
        return 1
    else:
        return fib(terms-1)+fib(terms-2)

terms = int(input("Enter the Number of Terms:\n"))
print(f"The {terms}th term of the fibonacci series is {fib(terms)}")