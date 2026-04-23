def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact =fact*i
    return fact
fact = factorial(5)
print("factorial:", fact)

# 5! = 5x4x3x2x1 = 120
#n! = n X (n-1) x (n-2) x...x1
