
n = int(input("n: "))

# define the factorial func
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(f"factorial of {n}:", factorial(n))

# s = 1! + 2! + 3! +... (n - 1)! + n!
fact = 1
s = 0

for i in range(1, n + 1):
    fact *= i
    s += fact
print("s =", s)