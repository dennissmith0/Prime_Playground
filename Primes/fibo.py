def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#print(fibonacci(10)) # 55
#print(fibonacci(20)) # 6765
    
'''This script will print out the first n+1 Fibonacci numbers, starting from 0.
Note that range(n+1) is used to include n in the range.

However, this is not efficient as it involves redundant computations.
The same Fibonacci numbers are calculated multiple times. For a large n,
this can take a very long time.'''  
if __name__ == "__main__":
    n = 11
    for i in range(n+1):
        print(fibonacci(i))

'''A more efficient approach would be to compute the Fibonacci numbers iteratively
and store them in a list as you go:
'''
def fibonacci(n):
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

'''This is much more efficient, as each Fibonacci number is calculated only once.'''
if __name__ == "__main__":
    n = 11
    fib = fibonacci(n)
    for num in fib:
        print(num)
