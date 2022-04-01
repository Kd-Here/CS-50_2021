from sys import argv

# if len(argv)==2:
#     print("Hello, "+argv[1])
# else:
#     print("Hello world")


# Learning how to remove first string that user put in command line
# for arg in argv:
#     if arg==argv[0]:
#         print(end="")
#     else:
#         print(arg)


# Alternative way to do this by using array from to from i.e

for arg in argv[1:]:
    print(arg)