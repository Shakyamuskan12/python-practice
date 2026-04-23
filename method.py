a = {
    "name" : "Pninfosys",
    "college" : "RJIT",
   #"college" : "ITM",  #Duplicates Not allowed
   "mark" : [1,2,3,4], #list
   "education" : {'ram': 'MCA'},
   1 : 2,
}

# print(a["college32"])
# print(a.get("college1")) #(error ki bhja none show hoga get method se)
# print(a.keys())
# print(type(a.keys())
# print(list(a.keys()))
# print(a.values())
# print(a.items())

#update dictionary
#print(a)

# updatedict = {
#     "branch" : "it",
#     "phone" : 9854273627,
#     "salary" : 4000,
#     "name" : "rohit"  #update
# }

# a.update(updatedict)    #update the dictionary
# print(a)

#print(a["college232"]) # ye error dega
# print(a["college"]) # usse error ki bhja se ye print nhi hoga python line by line chlti hai isliye bahi ruk jayegi 

try:
    print(a["college232"])
except Exception as w:
    print(w)

print(a["college"])  # try lgane ke bd ye print ho sakta hai 
