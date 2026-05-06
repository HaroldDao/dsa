# fibonacci
# f(n) = f(n - 2) + f(n - 1) 
# 1 1 2 3 5 ... f(n - 2) + f(n - 1)

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

f = int(input("f: "))

for i in range (1, f + 1):
    print(fibonacci(i), end=", ")

print(f"\nfibonacci({f}):", fibonacci(f))