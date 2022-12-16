arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
total=0
for i in range(len(arr)):
    total=total+int(arr[i][i])
print(total)