def sum_n(n):
    if n ==1:
        return 1
    else:
        return n + sum_n(n-1)
print(sum_n(5))

#5+4+3+2+1 = 15