#prime number check funtion 

def is_prime(num):
    if num <=1:
       return "Not prime"
    for i in range(2, num):
        if num % i ==0:
           return "Not prime"
    return "prime"
print(is_prime(1))