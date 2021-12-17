# Recursive Function
# input: which fibonacci number?
n = int(input())
d = [0] * (n+1)

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # Return if already calculated previously
    if d[x] != 0:
        return d[x]
    # Calculate if not yet calculated
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# return the nth fibonacci number
fibo(n)
