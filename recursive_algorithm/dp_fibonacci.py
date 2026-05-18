def fibonacci(n):
    res = 1
    if n <= 2:
        return res
    else:
        fib1 = fib2 = 1
        for i in range(3, n + 1):
            res = fib1 + fib2
            fib1 = fib2
            fib2 = res
        return res

print(fibonacci(20))