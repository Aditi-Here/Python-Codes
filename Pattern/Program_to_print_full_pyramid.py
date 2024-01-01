n = 5
for i in range(n,0,-1):
    for j in range(n):
        if (j+2)>i:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print('\r')

