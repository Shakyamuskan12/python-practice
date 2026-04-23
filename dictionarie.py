#dictionaries ke ander multiple data store kar sakte hai
#Dictionaries are used to store data values in key:value pairs
#Dictionaries is a collection of key value pairs 
a ={

    "name": "pninfosys rohit",
    "college":"rjit",
    #"phone":324565,
    2 : [1,2,3,4,1,1,(2,4,5,5)], #listprint(a["education"]['ram'])

    4: ("ram","mohit"), #key : value
   "education": {'ram':'MCA'},
   "city" : "gwalior",

}
# print(a)
# print(type(a))
# print(a["name"])
# print(a[4])
# print(a[0])  #key error
# print(a[2][6]) 
# print(type(a[2][6]))
# print(a["education"]["ram"][2])
# print(a["city"][1])
# print(type(a["city"]))
# print(a["city"])


#change dictionary items (dictionary mutuable hai hum change kar sakte hai usse)
#print(type[(a[4]))
# print(a)
a[4] =(40,50,60,70,87,5,9)
a["name"]="raj"
print(a)


