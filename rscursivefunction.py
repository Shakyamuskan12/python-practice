def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

#n! = n x (n - 1)!

#fact(5)
# 5 * fact(4)

#fact(4)
# 4 * fact(3)

#fact(3)
# 3 * fact(2)

#fact(2)
# 2 * fact(1)

#fact(1)
# 1 * fact(0)

#fact(0)
1

#fact(0) = ab yahan se calculation start hoti hai.
#fact(0) = 1 x 1 = 1
#fact(0) = 2 x 1 = 2
#fact(0) = 3 x 2 = 6
#fact(0) = 4 x 6 = 24
#fact(0) = 5 x 24 = 120

