# Here we are going to find average of numbers provided by user

n=int(input("HEY user please enter your subject number\n"))
marks=[]*n
for i in range(n):
    a =int(input(f"Enter the {i} subject marks:-"))
    marks.append(a)
print(*marks, sep=", ", end=" respectively!")
total=sum(marks)
avg=total/n
print(f"\mHello your average is {avg}")
