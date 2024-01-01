# Program to print half pyramid using *
for i in range(7):
    for j in range(i+1):
        print('*',end=" ")
    print('\n')


for i in range(7):
    for j in range(7-i):
        print('*',end="")
    print('\n')