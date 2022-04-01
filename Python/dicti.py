#Here we are looking how to use dictionary in python
# https://youtu.be/ky-24RvI57s?t=7410
a=input("Enter the name you wanted to find:-")

Mydict={
    "Kd":'99',
    "Vit":"33",
    "Ruk":"98"
}

if a in Mydict:
    #This means in dictionary go to value or go to index of a
    find=Mydict[a]
    print(f"ID:-{find}")
else:
    print("Not here")

# if a in Mydict:
#     print(Mydict.get(a))
# else:
#     print("WE didn't found that")
    
