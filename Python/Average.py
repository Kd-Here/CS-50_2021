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

# How to change the name of commit using vscode put this is terminal
# git commit --amend -m "Here give the new name or mssg for commit"
#  git push --force origin master

# Sort trick if you wanted to edit the message of any file or folder move to that and 
#  click on git option below run and see source control there write mssg in Message
# And then you can press ctrl + Enter and pop arise creaate blank commit yes then see