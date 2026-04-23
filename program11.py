def fib(n):
    if n <=1 :
        return n  # stop
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))

# 0 1 1 2 3 5 8
# f(n) = f(n-1) + f(n-2)
# 6 + precious 2 numbers ka sum 
#setup

#fib(6) = fib(5) + fib(4)
#fib(5) = fib(4) + fib(3)
#fib(4) = fib(3) + fib(2)
#fib(3) = fib(2) + fib(1)
#fib(2) = fib(1) + fib(0)

# fib(1) = 1
# fib(0) = 0

# fib(2) = 1 + 0 =1
# fib(3) = 1 + 1 =2
# fib(4) = 2 + 1 =3
# fib(5) = 3 + 2 =5
# fib(6) = 5 + 3 =8

