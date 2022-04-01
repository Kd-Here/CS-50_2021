#We are printing the exit statement here!
# Exit commands are helpful for higher level programming if they detect different they show different outcomes

# from sys import argv, exit

# if len(argv)!=2:
#     print("Missing something here!")
#     exit(1)

# print(f"Hello, {argv[1]}")
# exit(0)

#If we don't know about the name of sub module to import then we can import whole and can use

import sys

if len(sys.argv)!=2:
    print("Missing command-line argv")
    sys.exit(1)

print(f"hello,{sys.argv[1]}")
sys.exit(0)