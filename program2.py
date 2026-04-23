def check(num):
    if num % 2 ==0:
        print("even number")
    else:
        print("odd number")
check(2)

def check_even_odd(num):
    if num %2 ==0:
        return "Even"
    else:
        return "odd"
result =check_even_odd(3)
print(result)