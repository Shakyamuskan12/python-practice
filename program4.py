#maxmun number function

# def find_max(a,b,c):
#     return max(a,b,c) # built-in function
# print("max: ", find_max(10,30,29)) 

#interview
def find_max1(a,b,c):
    if a>=b and a>=c:
        return a
    elif b >=a and b >=c:
        return b
    else:
        return c
    print("max: ", find_max1(10,30,29))