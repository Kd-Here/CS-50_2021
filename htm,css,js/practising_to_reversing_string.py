# Here we are lookin how to use i=i+2 or i=i+3 in python since
# IN python we don't have i=i+2 or something like that we can use 
# In python we had i+=2 so we can't use that in loops we had another way which is
#  for i in range(0,9,3) here 0 is start and 9 is end of loop and 3 is interval which is same as i=i+3


a=input("Enter the search querey\n")
b=len(a)
print("\nThe reverse of the string is:-")
for i in range(b-1,-1,-1):
    print(a[i],end="")
